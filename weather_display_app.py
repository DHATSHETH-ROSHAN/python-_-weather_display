# importing all the necessary libraries

# bs4 for importting beautifulsoup to do webscraping
# requests to handle html links to connect and retrive datas
# win10toast to do notifiction on this thing
# geocoder to get the current location of the user

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import geocoder
import logging
#import time
#import schedule

# initialize the notifier app 
n = ToastNotifier()

# configure logging
logging.basicConfig(filename='weather_app.log', level=logging.INFO, format='%(asctime)s - %(message)s')


# to gather raw data from the given link
def getdata(url):
    try: 
        r = requests.get(url, timeout = 10)
        r.raise_for_status()    # this will the error code caused
        return r.text
    except Exception as e:
        logging.error(f"Error fetching data from URL: {e}")
        return None

#get the users current location using the geocoder

def get_location():
    try: 
        g = geocoder.ip('me')   # using the ip to track down the location of the user
        if not g.latlng:
            raise Exception("Unable to feth the location coordinates")        
        return g.latlng         # returns the latitude and longitude of user ass list [latitude, longitude]
    except Exception as e:
        logging.error(f"Error fetching location: {e}")
        return None, None, "Unknown Location"


# fallback function for openweatherMap
def open_weathermap(lat,long, api_key =  "4fdc66bb5ae5f437640e9a50f68fbfa7"):        # replace this "API_key" = 4fdc66bb5ae5f437640e9a50f68fbfa7  with your own api key
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=metric&appid={api_key}"
        response = requests.get(url).json()
        city = response['name']
        temp = response['main']['temp']
        rain = response.get('rain', {}).get('1h', 0) #rain in the last hour
        return f"Weather in {city}:\nTemperature: {temp}°C\nRain (last hour): {rain} mm"
    except Exception as e:
        logging.error(f"Error fetching weather from OpenWeatherrMap: {e}")
        return "Unable to fetch weather details from the openweatherMap."

def fetch_weather():
    #to handle the errors occured on this 
    try:
        # retrive the location details of the user
        lat, long = get_location()
        if not lat or not long:
            raise Exception("Unable to fetch location. Checck your internet connection")
            
        
        # now retrive tthe locations data using the weaather.com 
        url = f"https://weather.com/en-IN/weather/today/l/{lat},{long}?par=google&temp=c"
        
        # fetch the weather data  
        htmldata = getdata(url)
        if not htmldata:
            raise Exception("Failed to fetch the weather.com using fallbackweather api.")
        
        # Parser weeather data
        soup = BeautifulSoup(htmldata, 'html.parser')
        # now to find out the requred details and filter tthem usng these to give output
        
        #current_temp = soup.find_all("span",class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
        #chances_rain = soup.find_all("div",class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
        current_temp = soup.select_one("span[data-testid='TemperatureValue']")
        chances_rain = soup.select_one("div[data-testid='PrecipitationValue']")
    
        if not current_temp or not chances_rain:
                raise Exception("Unable to parse weather details. The structure of the webpage might have changed.")
        # converrting the parsed details to string , to make it more readable
        temp =current_temp.text
        rain = chances_rain.text
        
        # prepare the result string with location details
        result = f"Weather in  \n Current temperature: {temp}°C \n Chances of rain: {rain}"
    except Exception as e:
        logging.warning(f"Error with Weather.com: {e}")
        result = open_weathermap(lat, long)
        
    # adding icon to the weather 
    icon = "🌞" if "sunny" in result.lower() else "☁️"
    res_ic = f"{icon} {result}"
    # show the notification with the live weatther update
    n.show_toast("live Weather update", res_ic, duration = 10)
    logging.info(f"weather update: {result}")
fetch_weather()

# now the code only works whenever you run this code instead if you want to make it run automatically for evry hours 
# below code will do that

#schedule.every(1).hours.do(fetch_weather)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

