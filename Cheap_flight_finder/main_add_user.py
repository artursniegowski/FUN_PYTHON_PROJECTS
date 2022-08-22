# program to run separently !! - used for addin users to our spreadsheet

from data_manager import DataManager
# env variables !
from dotenv import load_dotenv
load_dotenv()
import os


#==============================================================================
# sensitive data - you need to register and obtain your own !!
# your sheety endpoint and SECRET TOKEN
# API : https://sheety.co/
API_SHEETY_END_POINT_USERS = os.environ.get('API_SHEETY_END_POINT_USERS')
API_SHEETY_BASIC_PASSWORD = os.environ.get('API_SHEETY_BASIC_PASSWORD')
#==============================================================================

# main content of the program
# creating object hanlding our spreadsheetwith users
spread_sheet_users_handler = DataManager(sheety_end_point=API_SHEETY_END_POINT_USERS, 
                                        api_sheety_basic_password=API_SHEETY_BASIC_PASSWORD)


MESSAGE_WELCOME = "Welcome to Art's Flight Club."
MESSAGE_FIRST_NAME = "What is your first name?\n"
MESSAGE_LAST_NAME = "What is your last name?\n"
MESSAGE_EMAIL = "What is your email?\n"
MESSAGE_EMAIL_AGAIN = "Type your email again.\n"


print(MESSAGE_WELCOME)
first_name = input(MESSAGE_FIRST_NAME).strip()
last_name = input(MESSAGE_LAST_NAME).strip()
email_adrres_first = input(MESSAGE_EMAIL).strip()
email_adrres_again = input(MESSAGE_EMAIL_AGAIN).strip()

if email_adrres_first == email_adrres_again:
    spread_sheet_users_handler.create_a_row(data_name='user',
                                            firstName=first_name,
                                            lastName=last_name,
                                            email=email_adrres_first)
    print("Sucess!! Your email has beed added.")
else:
    print(f"The email you have entered dosent match. {email_adrres_first} is not the same as {email_adrres_again}")