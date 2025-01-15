# Live Weather Update Notification
This Python program provides live weather updates using data scraped from Weather.com and falls back to the OpenWeatherMap API in case of any issues. The program also fetches the user's current location automatically using the geocoder library and displays weather notifications on the desktop using win10toast.

## Features

Real-Time Location Detection: Automatically detects the user's current location using the geocoder library.

Weather Data Scraping: Retrieves temperature and precipitation details from Weather.com.

Fallback API Support: If Weather.com fails, the program fetches weather data from OpenWeatherMap.

Desktop Notifications: Displays weather updates as desktop notifications using win10toast.

Error Logging: Logs errors and issues to a file for debugging.

Custom Icons: Adds weather-specific icons like 🌞 or ☁️ in notifications.

## Requirements

Ensure the following Python libraries are installed:

requests (for making HTTP requests)

bs4 (for parsing HTML via BeautifulSoup)

win10toast (for desktop notifications)

geocoder (for detecting the user's current location)

To install all dependencies, run:
```
pip install requests beautifulsoup4 win10toast geocoder
```

## Configuration
OpenWeatherMap API Key:
Register for an API key at OpenWeatherMap.
Replace the placeholder "4fdc66bb5ae5f437640e9a50f68fbfa7" in the code with your actual API key.

## How to Run
Clone or download the repository to your local machine.
Open a terminal in the project directory and execute the script:
```
python weather_display_app.py
```
The program will:

Detect your current location.
Retrieve the weather details for your location.
Display a desktop notification with the temperature and rain chances.

## Code Overview

### Libraries Used
requests: For making HTTP requests to fetch weather data.
BeautifulSoup: For parsing and scraping HTML content from Weather.com.
win10toast: For displaying desktop notifications.
geocoder: For determining the user's current location based on their IP address.
logging: For logging errors and updates to a file (weather_app.log).

### Key Functions
getdata(url): Fetches raw HTML data from the provided URL.
get_location(): Retrieves the user's latitude and longitude using their IP address.
open_weathermap(lat, long, api_key): Fetches weather data using OpenWeatherMap's API as a fallback.
fetch_weather(): Retrieves weather details, handles errors, and displays notifications.

### Error Handling and Logging
Errors encountered during data retrieval, parsing, or location detection are logged in weather_app.log.
If Weather.com fails to provide data, the program automatically falls back to OpenWeatherMap for weather updates.

## Example Output
A sample notification might look like this:
referrence image = weather app.png
🌞 Weather in Your City
Current temperature: 25°C
Chances of rain: 10%

## License
This project is open-source and available under the MIT License.

## Future Improvements
Add more detailed weather metrics (e.g., wind speed, humidity).
Support for multiple weather providers for increased reliability.
GUI support for a more user-friendly experience.
