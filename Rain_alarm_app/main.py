#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

## ===================================== ##
# FILL IN YOUR LOCATION !!!
# https://www.latlong.net/
MY_LATITUDE = 52.406376
MY_LONGITUDE = 16.925167
# check if it actually rains
# https://www.ventusky.com/?p=39;-3;1&l=rain-3h
## ===================================== ##

# geeting env variables for TWILIO
account_sid = os.environ.get('ACCOUNT_SID_TWILIO')
auth_token = os.environ.get('AUTH_TOKEN_TWILIO')

# getting API key for OPEN_WEATHER_MAP
OPEN_WEATHER_MAP_API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')

# API - weather endpoint
OPEN_WEATHER_MAP_BASE_END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

# params for the weather api
OPEN_WEATHER_MAP_PARAMETERS = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": OPEN_WEATHER_MAP_API_KEY,
}

# making the request
request = requests.get(url=OPEN_WEATHER_MAP_BASE_END_POINT, 
                        params=OPEN_WEATHER_MAP_PARAMETERS)

# checking for error 
request.raise_for_status()

# getting only the first 12 hours of data - only param id for each hour
# base on the id parameter we can determin wheather it is going to rain
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# if the id is under 700 it means it is some kind of rain or bad weather
# if there is any true value, any will return True
will_rain_in_next_12_hours = any([data_inner['id']<700 for hour_data \
    in request.json()['hourly'][:12] for data_inner in hour_data['weather']])


if will_rain_in_next_12_hours:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER", # you need to adjust this number
        to="YOUR TWILIO VERIFIED REAL NUMBER"  # you need to adjust this number
    )
    print(message.status)