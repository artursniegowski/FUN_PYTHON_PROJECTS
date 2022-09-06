import requests
from datetime import datetime
from email_manager import EmailManager
from time import sleep

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

# user defined email and app password - has to be GMAIL !
MY_EMAIL = os.environ.get('MY_EMAIL')
APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

# position of your location
# can be checked here https://www.latlong.net/
MY_LAT = 51.366143 # Your latitude
MY_LONG = 17.942096 # Your longitude

# creating an email writer object
email_writer = EmailManager(email_app_password=APP_PASSWORD,email_from=MY_EMAIL)
# email adress where we want to send the email to about ISS possible viewing
EMAIL_RECIVER = "example@proton.me" # Set this email !


#Your position is within +5 or -5 degrees of the ISS position.
def ISS_position_is_close(latitude: float, longitude: float) -> bool:
    """
    returns true if the current position of ISS is withinn +/- 5 degrees
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    print(iss_latitude,iss_longitude)

    if  (latitude - 5) < iss_latitude < (latitude + 5) and \
        (longitude - 5) < iss_longitude < (longitude + 5):
        return True
    else:
        return False

    

def is_currently_dark(latitude: float, longitude: float) -> bool:
    """
    return true if for the given position curently is night time
    """
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    #print(sunrise,sunset,current_hour)

    if sunrise < current_hour < sunset:
        return False
    else:
        return True

while True:
    #If the ISS is close to my current position
    # and it is currently dark
    if ISS_position_is_close(latitude=MY_LAT, longitude=MY_LONG) and \
        is_currently_dark(latitude=MY_LAT, longitude=MY_LONG):
        # Then send me an email to tell me to look up.
        email_writer.send_gmail_mail(email_title="ISS is here!!", 
                                    message_to_send="LOOK UP!! ISS is here", 
                                    email_to=EMAIL_RECIVER)
    else:
        print("ISS is not visible!")


    sleep(100)