# stock monitoring program
import requests
from email_manager import EmailManager

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os


# ==============================================================================
# Fill in the stock name you are interested in !
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# sending email to:
EMAIL_RECIVER = "example@proton.me" # Set this email !
# ==============================================================================
EMAIL_POSTIVE_CHANGE = lambda company_name, change_abs: f"{company_name}: UP {change_abs}%"
EMAIL_NEGATIVE_CHANGE = lambda company_name, change_abs: f"{company_name}: DOWN {change_abs}%"
EMAIL_TITLE = lambda was_positive_change, company_name, change_abs :  \
    EMAIL_POSTIVE_CHANGE(company_name, change_abs) if was_positive_change else \
        EMAIL_NEGATIVE_CHANGE(company_name, change_abs)
EMAIL_CONTETN = lambda data1, data2, data3 : f"Headline_1: {data1['title']}\nBrief_1: {data1['description']}\n\nHeadline_2: {data2['title']}\nBrief_2: {data2['description']}\n\nHeadline_3: {data3['title']}\nBrief_3: {data3['description']}"
# ==============================================================================


# sensitive data 
# user defined email and app password - has to be GMAIL !
MY_EMAIL_GMAIL = os.environ.get('MY_EMAIL_GMAIL')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
# API key for https://www.alphavantage.co/
ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
# API key for https://newsapi.org/
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


# creating an email writer object
email_writer = EmailManager(email_app_password=GMAIL_APP_PASSWORD,
                            email_from=MY_EMAIL_GMAIL)


## Use https://www.alphavantage.co API for stock price checking 
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get the news.
ALPHA_VANTAGE_API_BASE_END_POINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY,
}
request = requests.get(url=ALPHA_VANTAGE_API_BASE_END_POINT,
                        params=ALPHA_VANTAGE_PARAMS)
request.raise_for_status() # check if any errors occured
# returns the whole data - daily 
data_all_daily = request.json()['Time Series (Daily)']
# returns only the last two days - closing value
last_two_days = {key: data_all_daily[key]['4. close'] for key in list(data_all_daily)[:2] }
date_of_last_price = list(last_two_days)[0]
yesterda_value = float(list(last_two_days.values())[0])
day_before_yesterday_value = float(list(last_two_days.values())[1])
percentage_changed = round((yesterda_value-day_before_yesterday_value)/yesterda_value*100,2)
percentage_changed_was_positive = True if percentage_changed >= 0 else False
percentage_changed_abs = abs(percentage_changed)

# stock price change greater than 5% from previous day, get the news and send the email
if percentage_changed_abs > 5.0:

    # get news related to the company name
    ## Use https://newsapi.org
    # get the first 3 news pieces for the COMPANY_NAME.
    NEWS_API_BASE_END_POINT = "https://newsapi.org/v2/everything"
    NEWS_API_PARAMS = {
        "pageSize": 3,
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    request_news = requests.get(url=NEWS_API_BASE_END_POINT,
                            params=NEWS_API_PARAMS)
    request_news.raise_for_status() # check if any errors occured
    news_data = request_news.json()['articles']
    news_articles = []
    if len(news_data) >= 3: # at least 1 article
        # only last three articles - and only retriving the title and description
        news_articles = [{'title': article['title'], 'description': \
            article['description'][:200]} for article in news_data[:3]]

    #print(news_articles)

    # send email to the EMAIL_RECIVER with the info as:
    """
    TITLE: TSLA: UP 2% or TSLA: DOWN 5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
    and prominent investors are required to file by the SEC The 13F filings 
    show the funds' and investors' portfolio positions as of March 31st, near 
    the height of the coronavirus market crash.
    """
    #print(EMAIL_TITLE(percentage_changed_was_positive,STOCK,percentage_changed_abs))
    #print(EMAIL_CONTETN(news_articles[0],news_articles[1],news_articles[2]))
    #send email
    email_writer.send_gmail_mail(email_title=EMAIL_TITLE(percentage_changed_was_positive,STOCK,percentage_changed_abs).encode(encoding="ascii",errors="ignore").decode(), 
                                   message_to_send=EMAIL_CONTETN(news_articles[0],news_articles[1],news_articles[2]).encode(encoding="ascii",errors="ignore").decode(), 
                                   email_to=EMAIL_RECIVER)

else:
    print(f"The stock: {COMPANY_NAME} changed only {percentage_changed_abs}%")