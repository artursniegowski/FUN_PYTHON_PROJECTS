# Stock_news_monitoring_project

This program monitors the prices of a given stock and notifies the user via email if there is a good chance for investing, like big fluctuation in price. The threshold of fluctuation can be adjusted. By default, it is set to 5%. 
1. First, the program pulls out the data of the stock price that we are interested in. For the two previous days, the closing prices of the given company will be compared. Whether it went up or down and by how much. 
Here we will use the API: https://www.alphavantage.co/ </br>
2. Next, the program will fetch three news data regarding this company, which should make it easier to understand the reason for the fluctuation. 
Here we will use the API: https://newsapi.org/ </br>
3. At the end, the data is put together, and the program will send the user an email about the new finding. (this can be easily adjusted to send an SMS text instead with the help of https://www.twilio.com/) </br>


In the main.py we can adjust these variables: </br>
STOCK = "TSLA" - the stock short name - used to find the stock in the alphavantage API </br>
COMPANY_NAME = "Tesla Inc" - description for the stock name - used for finding the news </br>
EMAIL_RECIVER = "example@proton.me" - where the email is going to be sent </br>


Before using the program, we need to create a Gmail account that the program can use and generate an app_pssword for our account (https://help.prowly.com/how-to-create-use-gmail-app-passwords). We also need to acquire the keys for the https://www.alphavantage.co/ API and for the https://newsapi.org/ API which is completely free.
After obtaining the data, we have to change the name of .env.example to .env and fill in:</br>
MY_EMAIL_GMAIL = "YOUR_OWN@gmail.com"</br>
GMAIL_APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"</br>
ALPHA_VANTAGE_API_KEY = "YOUR_API_KEY_ALPHA_VANTAGE"</br>
NEWS_API_KEY = "YOUR_API_KEY_NEWS_API"</br>


The program was developed using python 3.10.05, smtplib, requests, APIs. 

In order to run the program, you have to execute the main.py.