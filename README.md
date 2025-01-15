# Live Weather Update Notification
This Python program provides live weather updates using data scraped from Weather.com and falls back to the OpenWeatherMap API in case of any issues. The program also fetches the user's current location automatically using the geocoder library and displays weather notifications on the desktop using win10toast.

## Features
Real-Time Weather Updates: Get live updates on the current temperature and chances of rain.
Automatic Location Detection: Uses your IP address to determine your current location (latitude and longitude).
Desktop Notifications: Displays weather updates as desktop toast notifications.
Fallback API: If Weather.com data is inaccessible, it uses OpenWeatherMap as a backup.
Error Handling: Logs errors and warnings to a file for debugging.

## Prerequisites
Before running the program, ensure you have the following installed:

Python 3.6+: Download Python
Required Libraries: Install the dependencies using pip:
bash
Copy code
pip install requests beautifulsoup4 win10toast geocoder

## Configuration
OpenWeatherMap API Key:
Register for an API key at OpenWeatherMap.
Replace the placeholder "4fdc66bb5ae5f437640e9a50f68fbfa7" in the code with your actual API key.

## How to Run
Clone or download the repository to your local machine.
Open a terminal in the project directory and execute the script:
bash
Copy code
python weather_display.py
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

Copy code
🌞 Weather in Your City
Current temperature: 25°C
Chances of rain: 10%
License
This project is open-source and available under the MIT License.

## Future Improvements
Add more detailed weather metrics (e.g., wind speed, humidity).
Support for multiple weather providers for increased reliability.
GUI support for a more user-friendly experience.
