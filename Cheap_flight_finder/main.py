# This file will need to use the DataManager,FlightSearch, FlightData, 
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

# user defined !
ORIGIN_CITY_IATA = "WAW" # city of departure 

#==============================================================================
# sensitive data - you need to register and obtain your own !!
# your sheety endpoint and SECRET TOKEN
# API : https://sheety.co/
API_SHEETY_END_POINT_PRICES = os.environ.get('API_SHEETY_END_POINT_PRICES')
API_SHEETY_END_POINT_USERS = os.environ.get('API_SHEETY_END_POINT_USERS')
API_SHEETY_BASIC_PASSWORD = os.environ.get('API_SHEETY_BASIC_PASSWORD')
# GMAIL APP password
# user defined email and app password - has to be GMAIL !
MY_GMAIL_EMAIL = os.environ.get('MY_GMAIL_EMAIL')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
# your tequila api key, and the endpoint
# API : https://partners.kiwi.com/
API_TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
API_TEQUILA_KEY = os.environ.get('API_TEQUILA_KEY')
#==============================================================================

# main content of the program
# creating object hanlding our spreadsheet with flight prices
spread_sheet_data_handler = DataManager(sheety_end_point=API_SHEETY_END_POINT_PRICES, 
                                        api_sheety_basic_password=API_SHEETY_BASIC_PASSWORD)

# creating object hanlding our spreadsheetwith users
spread_sheet_users_handler = DataManager(sheety_end_point=API_SHEETY_END_POINT_USERS, 
                                        api_sheety_basic_password=API_SHEETY_BASIC_PASSWORD)

# creating object hanlling flight search
flight_search_handler = FlightSearch(tequila_api_end_point=API_TEQUILA_ENDPOINT,
                                     tequila_api_key=API_TEQUILA_KEY)

# creating an email writer object
email_writer = NotificationManager(email_app_password=GMAIL_APP_PASSWORD,
                            email_from=MY_GMAIL_EMAIL)

# getting data from our spreadsheet
# getting flight data from 'prices' spreadsheet
spreadsheet_flight_data = spread_sheet_data_handler.return_data_from_table(data_name='prices')
# gettign users data from 'users' spreadheet
spreadsheet_users_data = spread_sheet_users_handler.return_data_from_table(data_name='users')

#print(spreadsheet_flight_data)
# updating IATA code if not existing
for data in spreadsheet_flight_data:
    if data['iataCode'] == '': # if the column IATA Code is empty - update it
        # find the IATA CODE
        IATA_code = flight_search_handler.get_destination_code(data['city'])
        spread_sheet_data_handler.update_a_row(row_num_to_update=data['id'],iataCode=IATA_code)




# Searching for Flights
# The next step is to search for the flight prices from ORIGIN_CITY_IATA to all the 
# destinations in the Google Sheet. In this project, we're looking only for 
# direct flights, that leave anytime between tomorrow and in 6 months (6x30days) 
# time. We're also looking for round trips that return between 7 and 28 days 
# in length. The currency of the price we get back should be in local currency, here PLN.
tomorrow_date = datetime.now() + timedelta(days=1)
six_month_time_from_now = datetime.now() + timedelta(days=180)

# checking the prices for the flights and if lower than defined treshold
# send a email with the flight deal
for destination in spreadsheet_flight_data:
    flight_data = flight_search_handler.check_flights(origin_city_code=ORIGIN_CITY_IATA,
                                        destination_city_code=destination['iataCode'],
                                        from_time=tomorrow_date,
                                        to_time=six_month_time_from_now)

    if flight_data:
        # if found a flight under our defined price treshold from the spreadsheet
        # send an email with the notification - flight deal
        print(flight_data)
        if flight_data.price < destination['lowestPrice']:
            email_writer.send_emails(
                list_of_users=spreadsheet_users_data,
                email_title='Low price allert!',
                message_to_send=flight_data.return_format_data_for_email(),
            )   
