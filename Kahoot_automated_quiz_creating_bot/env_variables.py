# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# env variables ! - dont change here !

USER_EMAIL_KAHOOT = os.environ.get('MY_EMAIL')
USER_EMAIL_KAHOOT_PASSWORD = os.environ.get('MY_EMAIL_PASSWORD')

################################################################################