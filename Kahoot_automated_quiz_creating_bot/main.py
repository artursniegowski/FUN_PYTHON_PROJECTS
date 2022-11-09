from bot_kahoot import KahootHandlerBot
from env_variables import USER_EMAIL_KAHOOT, USER_EMAIL_KAHOOT_PASSWORD


# path to the driver - adjust it !!
CHROME_DRIVER_PATH = "ChromeDriver_browser/chromedriver.exe"


list_places = []
with open('questions.txt','r') as f:
    list_places = f.readlines()

# kahoot bot object
kahoot_boot = KahootHandlerBot(CHROME_DRIVER_PATH)

# creating the quiz in kahoot
kahoot_boot.do_kahoot(
    USER_EMAIL_KAHOOT,
    USER_EMAIL_KAHOOT_PASSWORD, 
    list_places, 
    option_time=7,
    title=f'My Questions',
    description='Most interesting questions.')
