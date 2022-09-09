from twitter_bot import InternetSpeedTesterTwitterBot


####################### INTERNET PROVIDER SETTINGS #############################
# adjust this values to your liking ! or as per contract
# Mbps per second 
PROMISSED_DOWNLOAD_SPEED = 150 
PROMISSED_UPLOAD_SPEED = 50
################################################################################


####################### SELENIUM SETTINGS #########################
# adjust this path to wherever you have unpacked the chrome driver file !
# dont forget that the verion of chrome drive has to match the verison of chrome browser
# https://chromedriver.chromium.org/downloads
# relative path, you can use as well absolute path !
chrome_driver_path = "ChromeDriver_browser/chromedriver.exe"
#######################################################################


twitter_bot = InternetSpeedTesterTwitterBot(chrome_driver_path=chrome_driver_path)
if twitter_bot.get_internet_speed(): # if sucessfully get internet speed than tweet the info
    if float(twitter_bot.ulpoad_speed) < float(PROMISSED_UPLOAD_SPEED) or \
        float(twitter_bot.download_speed) < float(PROMISSED_DOWNLOAD_SPEED):

        twitter_bot.tweet_at_provider(
            promissed_download_speed=PROMISSED_DOWNLOAD_SPEED, 
            promissed_upload_speed=PROMISSED_UPLOAD_SPEED)
    else:
        # close tab if we dont have to complain about our internet speed
        twitter_bot.driver.quit() 