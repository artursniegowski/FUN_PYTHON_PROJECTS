# Exercise tracking app
import requests
from datetime import datetime

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

# =============================================================================
# your personal data !
GENDER = "male"
WEIGHT_KG = "70.5"
HEIGHT_CM = "176"
AGE = "33"
#==============================================================================
# sensitive data - you need to register and obtain your own !!
# API KEY and ID for nutritionix
# https://www.nutritionix.com/business/api
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_API_ID = os.environ.get('NUTRITIONIX_API_ID')
# your sheety endpoint and SECRET TOKEN
# API : https://sheety.co/
API_SHEETY_END_POINT = os.environ.get('API_SHEETY_END_POINT')
API_SHEETY_SECRET_TOKEN = os.environ.get('API_SHEETY_SECRET_TOKEN')
#==============================================================================

# awaiting user input
exercise_text = input("Tell me which exercises you did: ")

# nutritionix - print the exercise stats
NUTRITIONIX_API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Summary: Estimate calories burned for various exercises 
# using natural language.  Developer can optionally include user 
# demographics like age, gender, weight to make a more accurate 
# estimate for calories burned.

NUTRITIONIX_API_HEADER = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    #'x-remote-user-id': '0',
}

NUTRITIONIX_API_DATA = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

respond = requests.post(url=NUTRITIONIX_API_END_POINT,
                        json=NUTRITIONIX_API_DATA,
                        headers=NUTRITIONIX_API_HEADER)

respond.raise_for_status() # check for errors
nutritionix_data = respond.json()['exercises']



# updating spred sheets using
# API : https://sheety.co/
# Thousands of people are using Sheety to turn their spreadsheets 
# into powerful APIs to rapidly develop prototypes, websites, apps and more.
# 
# first you have to create an spredsheet in google docs while loged in your account, 
# the spread sheet shoudl have columns: Date,Time,Exercise,Duration,Calories.
# next while loged to your gmail account you should log in to sheety.co and crete a new project
# adding the url of you spreadsheet you have just creted, 
# and enable the GET and POST request for the API


current_day = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

API_SHEETY_AUTHENTICATION_HEADER = {
    'Authorization':API_SHEETY_SECRET_TOKEN,
}

    # save data to the spreadsheet
for data in nutritionix_data:
    API_SHEETY_DATA = {
        'workout': {
            'date':current_day,
            'time':current_time,
            'exercise':data['name'].title(),
            'duration':data['duration_min'],
            'calories':data['nf_calories'],
        }
    }

    respond_sheety = requests.post(url=API_SHEETY_END_POINT,
                                json=API_SHEETY_DATA,
                                headers=API_SHEETY_AUTHENTICATION_HEADER)
    respond_sheety.raise_for_status()
    #data_sheety = respond_sheety.json()
    #print(data_sheety)