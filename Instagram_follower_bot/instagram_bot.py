# class for handling the instagram bot

from selenium import webdriver
from selenium.common.exceptions import  ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os


################################################################################
## sensitive data ###
#####################
# user defined email and app password for your Instagram account !
# env variables !! - dont change here !!
MY_INSTAGRAM_EMAIL = os.environ.get('MY_INSTAGRAM_EMAIL')
MY_INSTAGRAM_PASSWORD = os.environ.get('MY_INSTAGRAM_PASSWORD')
################################################################################


class InstagramBotSettings:
    """
    settings for the Instagram bot
    """
    WEBSITE_URL_INSTAGRAM_LOGIN = "https://www.instagram.com/accounts/login/"
    WEBSITE_URL_INSTAGRAM_LOGOUT = "https://www.instagram.com/accounts/logout/"
    WEBSITE_URL_INSTAGRAM = "https://www.instagram.com/"



class InstagramFollowBot:
    """
    class for handling selenium, and instagram follow bot 
    """
    def __init__(self, chrome_driver_path:str) -> None:
        #  creating service for the chrome driver
        self.chrome_driver_service = Service(chrome_driver_path)
        # creating the webdriver
        self.driver = webdriver.Chrome(service=self.chrome_driver_service)

    
    def _wait_for_presence_of_element(self, wait_time_sec: int, locator_strategy: By, 
        selector: str, error_message: str) -> WebElement | bool:
        """
        function to wait for an element presence, and then returns this element
        if not found in a given time a Timeout exception will occure and the function will close the driver and 
        return False
        """
        try:
            results_element = WebDriverWait(self.driver, wait_time_sec).until(
                EC.presence_of_element_located((locator_strategy, selector))
            )
            return results_element
        except TimeoutException as timeout_ex:
            print(type(timeout_ex))
            print(error_message)
            # quitting / closing the driver
            self.driver.quit()
            return False


    def login(self) -> bool:
        """
        login to your instagram account.
        returns True if success and False if fails.
        """
        self.driver.get(InstagramBotSettings.WEBSITE_URL_INSTAGRAM_LOGIN)

        # wait for page to load
        # time.sleep(3)

        login_username_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.CSS_SELECTOR,
            selector='input[name="username"]',
            error_message="Cant find the username input on the login page",
        )
        if not login_username_element: return False

        login_username_element.send_keys(MY_INSTAGRAM_EMAIL)
        login_password_element = self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
        login_password_element.send_keys(MY_INSTAGRAM_PASSWORD)

        time.sleep(1)
        # login !
        login_password_element.send_keys(Keys.ENTER)

        # wait for the homepage to load - waiting for the homepage login logo
        logo_hompage_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.CSS_SELECTOR,
            selector="div[data-testid='instagram-homepage-logo']",
            error_message="Cant find the homepage after login. Looking for login logo!",
        )
        if not logo_hompage_element: return False

        # giving soem extra time to load
        time.sleep(1)

        return True


    def find_followers(self, instagram_account: str) -> bool:
        """
        finding followers for the given account name.
        returns True if success and False if fails.
        """
        # wait for the previous step to load the page
        #time.sleep(10)
        # changing the url to the user
        # https://www.instagram.com/star._.wars._.memes/
        self.driver.get(InstagramBotSettings.WEBSITE_URL_INSTAGRAM+f"{instagram_account}/")
        
        # try to fidn the button with followers
        followers_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.CSS_SELECTOR,
            # href=/star._.wars._.memes/followers/
            selector=f"a[href='/{instagram_account}/followers/']",
            error_message=f"Cant find the followers for the user {instagram_account}. Maybe the user:{instagram_account} doesn't exist!",
        )
        if not followers_element: return False

        # if followers exists press it to open the modal with the deatl view of all followers
        followers_element.click()

        # wait for the modal to appear
        # time.sleep(3)
        return_element = self._wait_for_presence_of_element(
            wait_time_sec=3,
            locator_strategy=By.CSS_SELECTOR,
            # href=/star._.wars._.memes/followers/
            selector="div[id='scrollview']",
            error_message=f"Cant find followers modal scrollview id that appears in the main view.",
        )
        if not return_element: return False

        # extra time to load
        time.sleep(1)

        # select the modal
        #modal_element = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]')
        modal_element = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")

        # every time the loops goes by the modal will be scrolled down
        # and more users will be loaded
        for _ in range(2):
            # scrolling down to load more followers
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal_element)
            time.sleep(2)

        return True


    def follow(self) -> bool:
        """
        function for following the followers of the target account.
        returns True if success and False if fails. 
        """
        follow_buttons_elements = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]//button")
        

        # going through each of the buttons and following the users
        if len(follow_buttons_elements) > 0:
            for follow_button in follow_buttons_elements:
                
                try:
                    follow_button.click()
                    # wait time so instagram doesnt think it's a bot
                    time.sleep(1)
                except ElementClickInterceptedException as intercept_exception:
                    # this occurse when we follow already the person and we get a popup window to unfollow
                    # in which case we have to press the cancle button
                    cancel_button_for_additonal_pop_up_window = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                    cancel_button_for_additonal_pop_up_window.click()
                    time.sleep(1)

        return True


    def logout(self) -> None:
        """
        function for log out from your instagram account.
        """
        # logout
        self.driver.get(InstagramBotSettings.WEBSITE_URL_INSTAGRAM_LOGOUT)
        # time to say goodbye
        time.sleep(5)
        # and exit the driver
        self.driver.quit()