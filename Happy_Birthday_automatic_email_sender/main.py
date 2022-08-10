from birthday_manager import CSVReaderManager
from email_manager import EmailManager
from random import choice

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os


# user defined email and app password - has to be GMAIL !
MY_EMAIL = os.environ.get('MY_EMAIL')
APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')


# file settings
FILE_NAME_BIRTHDAYS = "birthdays.csv"
LETTERS_TEMPLATES_NAMES = ['letter_1.txt','letter_2.txt','letter_2.txt']
LETTERS_TEMPLATES_FOLDER_NAME = 'letter_templates'
LETTER_TEMPLATE_DIRECTORY = lambda folder_name,letter_name : f"./{folder_name}//{letter_name}"



# returns a template letter
def return_template_wish_letter(file_name: str, word_to_replace: str, \
    new_replaced_name: str):
    """
    opens the template letter and replace the name with the given word, and returns
    the whole wish letter
    """
    try:
        with open(file_name,'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Could not find {file_name}")
        return None
    else:
        return data.replace(word_to_replace,new_replaced_name)


# creating email sender object
email_sender = EmailManager(email_app_password=APP_PASSWORD,email_from=MY_EMAIL)

# readidng the csv file with all the birthday data/ emails/ names
csv_reader = CSVReaderManager(FILE_NAME_BIRTHDAYS)
#data = csv_reader.return_data_as_dict()
data = csv_reader.return_current_day_birthday_data()

# if there is any match with current date birthday
if data:
    # looping through the whole list
    for person in data:
        message_wishes = return_template_wish_letter(
            file_name=LETTER_TEMPLATE_DIRECTORY(
                folder_name=LETTERS_TEMPLATES_FOLDER_NAME,
                letter_name=choice(LETTERS_TEMPLATES_NAMES)),
            word_to_replace='[NAME]',
            new_replaced_name=person['name'])

        # if a message was created send the email
        if message_wishes:
            email_sender.send_gmail_mail(email_title='Happy Birthday!',
                                    message_to_send=message_wishes,
                                    email_to=person['email'])