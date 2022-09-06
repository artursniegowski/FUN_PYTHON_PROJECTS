# ISS_tracker

This program tracks the position of the International Space Station (https://en.wikipedia.org/wiki/International_Space_Station), and once the station is visible at our location, it will send an automatic email reminding us to look up and search for the station.

The program uses the http://open-notify.org/Open-Notify-API/ISS-Location-Now/ API to determine the position of the ISS. 

The program uses the https://sunrise-sunset.org/api API to determine whether it is night or day time. 

In the main.py we have to set our location (which can be checked here https://www.latlong.net/) and the receiver email with the variables:</br>
MY_LAT = XX.XXX - Your latitude</br>
MY_LONG = XX.XXX - Your longitude </br>
EMAIL_RECIVER = "example@proton.me" - receiver email


Before using the program, we need to create a Gmail account that the program can use and generate an app_pssword for our account (https://help.prowly.com/how-to-create-use-gmail-app-passwords). 
After obtaining the data, we have to change the name of .env.example to .env and fill in MY_EMAIL = "EXAMPLE.USER@gmail.com" and
GMAIL_APP_PASSWORD = "GMAIL_APP_PASSWORD".


The program was developed using python 3.10.05, Email SMTP, datetime, requests, APIs. 

In order to run the program, you have to execute the main.py.