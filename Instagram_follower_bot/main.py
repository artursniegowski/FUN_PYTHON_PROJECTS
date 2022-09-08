from instagram_bot import InstagramFollowBot


####################### INSTAGRAM SETTINGS #############################
# adjust this account name to your liking !
# instagram account you want to replicate followers for. Figure out which 
# instagram account you would like to target. (Pick a large account that has 
# a lot of followers).
# this user has to exist in instagram
SIMILAR_INSTAGRAM_ACCOUNT = "name_of_the_instagram_account" # adjust this !!
################################################################################


####################### SELENIUM SETTINGS ######################################
# adjust this path to wherever you have unpacked the chrome driver file !      
# dont forget that the verion of chrome drive has to match the verison of 
# chrome browser
# https://chromedriver.chromium.org/downloads
# relative path, you can use as well absolute path !
CHROME_DRIVER_PATH = "ChromeDriver_browser/chromedriver.exe"
################################################################################

# creating instagram bot object
instagram_bot = InstagramFollowBot(CHROME_DRIVER_PATH)

if instagram_bot.login():
    if instagram_bot.find_followers(SIMILAR_INSTAGRAM_ACCOUNT):
        if instagram_bot.follow():
            instagram_bot.logout()