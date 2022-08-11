# Rain_alarm_app

This is an API driven application that will monitor the weather in the given location, and it will send automatically an SMS text in the morning to the defined number if it's going to rain. 

You can find your location using https://www.latlong.net/ .

For the weather forecast, the program will get hold of data from the API https://openweathermap.org/api, where you need to register and obtain your personal API key in order to be able to use this program.

For the SMS service, the program will use of https://www.twilio.com/. 

Before using the program, you will have to create a free account on https://openweathermap.org/api and a free account on https://www.twilio.com/. Next it will be required to adjust the name of .env.example to .env and adjust three variables :
OPEN_WEATHER_MAP_API_KEY, ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO - define with your obtained data. 


The program was developed using python 3.10.05, twilio, requests, API. 

In order to run the program, you have to execute the main.py.
