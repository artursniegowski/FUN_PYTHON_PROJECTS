# Happy_Birthday_automatic_email_sender

This is a python program that is an automated email birthday wish sender. It uses a spreadsheet with a list of birthdays, names, and emails, and based on the list, the program will check the current date. If that date matches someone's birthday from the file 'birthdays.csv' the program will extract the data and choose one of the random letters from the letter_templates directory and replace the name tag ([NAME]) with the matching name from birthdays.csv. At the end, the program will use a Gmail account to send a happy birthday email to this person.

Before using the program, we need to create a Gmail account that the program can use and generate an app_pssword for our account (https://help.prowly.com/how-to-create-use-gmail-app-passwords). 
After obtaining the data, we have to change the name of .env.example to .env and fill in MY_EMAIL = "EXAMPLE.USER@gmail.com" and
GMAIL_APP_PASSWORD = "GMAIL_APP_PASSWORD".


The program was developed using python 3.10.05, Email SMTP, datetime and Pandas. 

In order to run the program, you have to execute the main.py.

