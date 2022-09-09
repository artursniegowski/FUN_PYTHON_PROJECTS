# main program
from web_scrapper import AmazonScrapper
from notification_manager import NotificationManager

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
# SET THESE VARIABLES !!
# target price
TARGET_PRICE = 800.00
# COPY here your own url, amazon product url
AMAZON_PRODUCT_TO_TRACK_URL = "https://www.amazon.com/OnePlus-Smartphone-Unlocked-co-Developed-Hasselblad/dp/B07XM54RWB"
# email adress where we want to send the notification to, when the prices drops 
# below the given threshold
# dont forget to adjust !
EMAIL_RECIVER = "example@proton.me"#"example@proton.me" 
# define your header
# You'll need to pass along some headers in order for the request to return the actual website HTML
# go to http://myhttpheader.com/ to check these values and update them accordingly. 
MY_HTTP_HEADER = {
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
    "Accept-Encoding":"gzip, deflate", 
    "Accept-Language":"en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,de;q=0.6,la;q=0.5,ar;q=0.4",
    # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    # "Connection" : "keep-alive",
    "DNT":"1",
    "Connection" : "close",
    "Upgrade-Insecure-Requests":"1",
}
# MY_HTTP_HEADER = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
#     "Accept-Encoding":"gzip, deflate", 
#     "Accept-Language":"en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,de;q=0.6,la;q=0.5,ar;q=0.4",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
#     "DNT":"1",
#     "Connection":"close", 
#     "Upgrade-Insecure-Requests":"1"
#     }
################################################################################



################################################################################
## sensitive data ###
#####################
# user defined email and app password - has to be GMAIL !
# env variables ! - dont change here !
MY_EMAIL = os.environ.get('MY_EMAIL')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
################################################################################




# creating an email sender manager object for sending emails
email_sender_manager = NotificationManager(email_app_password=GMAIL_APP_PASSWORD
                                            ,email_from=MY_EMAIL)



####################scraping the data from given amazon url#####################
# creatign an object for scrapign data
amazon_scraper = AmazonScrapper(AMAZON_PRODUCT_TO_TRACK_URL, headers = MY_HTTP_HEADER)
product_price = amazon_scraper.return_the_price_of_product()
product_title = amazon_scraper.return_the_title_of_product()
# if price below our target price, send an email notification

if product_price: # if product price found
    print(product_price)
    if product_price <= TARGET_PRICE:
        # creating message for the email
        message_content = f"{product_title}\nnow:${product_price}\n{AMAZON_PRODUCT_TO_TRACK_URL}"
        # sending an email
        email_sender_manager.send_gmail_mail(email_title="Amazon Price Alert!", 
                                            message_to_send=message_content, 
                                            email_to=EMAIL_RECIVER)