from form_bot import FormHandlerBot
from web_scrapper import ZillowScrapper, ZillowScrapperSettings

####################### SELENIUM SETTINGS ######################################
# adjust this path to wherever you have unpacked the chrome driver file !      
# dont forget that the verion of chrome drive has to match the verison of 
# chrome browser
# https://chromedriver.chromium.org/downloads
# relative path, you can use as well absolute path !
CHROME_DRIVER_PATH = "ChromeDriver_browser/chromedriver.exe"
################################################################################


# scraping dat from zillow website
zillow_scrapper = ZillowScrapper(
    zillow_website_url=ZillowScrapperSettings.WEBSITE_URL_ZILLOW_PREDEFINED_SEARCH,
    headers=ZillowScrapperSettings.MY_HTTP_HEADER )

zillow_listings = zillow_scrapper.return_zillow_listing()

# filling in the data from the step above into google forms
forms_handler_bot = FormHandlerBot(CHROME_DRIVER_PATH)

if zillow_listings:
    forms_handler_bot.fill_in_data(zillow_listings)