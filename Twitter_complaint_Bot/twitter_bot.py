# class for handling the twitter bot , and speed test
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
# user defined email and app password for your Twitter account !
# env variables ! - dont change here !
MY_TWITTER_EMAIL = os.environ.get('MY_TWITTER_EMAIL')
MY_TWITTER_USERNAME = os.environ.get('MY_TWITTER_USERNAME')
MY_TWITTER_PASSWORD = os.environ.get('MY_TWITTER_PASSWORD')
################################################################################


class TwitterBotSettings():
    """
    settings for the twitter bot
    """
    WEBSITE_URL_FOR_SPEED_TEST = "https://www.speedtest.net/"
    WEBSITE_URL_TWITTER = "https://twitter.com/"


class InternetSpeedTesterTwitterBot():
    """
    class for handling selenium, intenret speed test,
    and twitter complaining 
    """
    def __init__(self, chrome_driver_path:str) -> None:
        #  creating service for the chrom driver
        self.chrome_driver_service = Service(chrome_driver_path)
        # creating the webdriver
        self.driver = webdriver.Chrome(service=self.chrome_driver_service)
        # setting the start download and upload speed of the curren user
        self.download_speed = 0
        self.ulpoad_speed = 0

  
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


    def get_internet_speed(self) -> bool:
        """
        getting the internet speed from the https://www.speedtest.net/,
        and updating the values download_speed, ulpoad_speed
        returning True if success , returning False if failed, bot terminated the speed test
        """
        self.driver.get(TwitterBotSettings.WEBSITE_URL_FOR_SPEED_TEST)
        # wait for the website to laod
        time.sleep(2)

        try:
            go_button_element = self.driver.find_element(By.CSS_SELECTOR, 'div.start-button a span.start-text')
            go_button_element.click()
        # if there is a pop a window, it will cover the access to our base window
        # The General Data Protection Regulation (GDPR) - accepting the pop up
        except ElementClickInterceptedException: 
            accept_gdpr_button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
            accept_gdpr_button.click()
            time.sleep(1)

            # try again and start the test
            try:
                go_button_element = self.driver.find_element(By.CSS_SELECTOR, 'div.start-button a span.start-text')
                go_button_element.click()
            
            except NoSuchElementException as no_element_ex:
                # something went wrong, couldent find the start test button
                print(type(no_element_ex))
                print("Error: Cant find the start button")
                # quitting / closing the driver
                self.driver.quit()
                return False

        # waiting for the test to finish or throw exception TimeOut
        # when it does a div with result-container-speed-active appears
        # so the bot will wait for it, but the max timeout will be 80 seconds
        results_element = self._wait_for_presence_of_element( 
                                            wait_time_sec=80,
                                            locator_strategy=By.CLASS_NAME,
                                            selector='result-container-speed-active',
                                            error_message="Error: Cant find the results after the test started! Waited 80 sec.",)
        if not results_element: return False
        # try:
        #     results_element = WebDriverWait(self.driver, 80).until(
        #         EC.presence_of_element_located((By.CLASS_NAME,'result-container-speed-active'))
        #     )
        # except TimeoutException as timeout_ex:
        #     print(type(timeout_ex))
        #     print("Error: Cant find the results after the test started! Waited 80 sec.")
        #     # quitting / closing the driver
        #     self.driver.quit()
        #     return False

        # if we found the cointainer with the results
        # we can now start taping into the values of the cointainer
        print("Speed test done.")
        ulpoad_speed_element = results_element.find_element(By.CLASS_NAME,'upload-speed')
        download_speed_element = results_element.find_element(By.CLASS_NAME,'download-speed')
        
        print("Upload and download speed updated!")
        self.ulpoad_speed = ulpoad_speed_element.text
        self.download_speed = download_speed_element.text

        return True


    def tweet_at_provider(self, promissed_upload_speed: int, promissed_download_speed: int) -> bool:
        """
        sends a tweet at the internet's providers twitter website if the 
        internet speed is under the promised speed
        if succesful return true / otherwise return false
        """
        self.driver.get(TwitterBotSettings.WEBSITE_URL_TWITTER)
        # wait for the website to load
        time.sleep(3)

        try :
            # login to twitter
            login_button_element = self.driver.find_element(By.CSS_SELECTOR,"a[href='/login'] div span")
            login_button_element.click()

        # if there is a pop a window, it will cover the access to our base window
        # so if there is a cookies popo up we will accept them
        except ElementClickInterceptedException:
            accept_cookies_button = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
            accept_cookies_button.click()
            time.sleep(1)

            # login to twitter
            login_button_element = self.driver.find_element(By.CSS_SELECTOR,"a[href='/login'] div span")
            login_button_element.click()
            # time.sleep(4)

        # wait for the login modal to appear
        user_email_input_element = self._wait_for_presence_of_element( 
                                    wait_time_sec=30,
                                    locator_strategy=By.CSS_SELECTOR,
                                    selector="div[aria-labelledby*='modal-header'] input[name*='text']",
                                    error_message="Error: Cant find the login input.",)
        if not user_email_input_element: return False
        
        # if login modal found , we will fill out the form with our email addres and with enter move to the next form
        # user_email_input_element = login_modal_element.find_element(By.CSS_SELECTOR,"input[name*='text']")
        user_email_input_element.send_keys(MY_TWITTER_USERNAME)
        time.sleep(1)
        user_email_input_element.send_keys(Keys.ENTER)

        # wait for the password to appear
        password_input_element = self._wait_for_presence_of_element( 
                                    wait_time_sec=30,
                                    locator_strategy=By.CSS_SELECTOR,
                                    selector="div[aria-labelledby*='modal-header'] input[name*='password']",
                                    error_message="Error: Cant find the password input.",)
        if not password_input_element: return False

        # puting down the password and log in to your account
        password_input_element.send_keys(MY_TWITTER_PASSWORD)
        time.sleep(1)
        password_input_element.send_keys(Keys.ENTER)
        time.sleep(2) 



        # waiting for the tweet field to appear
        tweet_text_element = self._wait_for_presence_of_element(
                                    wait_time_sec=30,
                                    locator_strategy=By.CSS_SELECTOR,
                                    selector="div.DraftEditor-root [data-text='true']",
                                    error_message="Error: Cant find the tweet text input.",)
        if not tweet_text_element: return False

        # filling the tweet
        tweet_text_element.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_speed}down/{self.ulpoad_speed}up when i pay for {promissed_download_speed}down/{promissed_upload_speed}up?")


        # send the tweet
        # waiting to find the tweet button
        tweet_button_element = self._wait_for_presence_of_element(
                                    wait_time_sec=30,
                                    locator_strategy=By.XPATH,
                                    selector='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]',
                                    error_message="Error: Cant find the tweet button.")
        if not tweet_button_element: return False

        time.sleep(1)
        # sending the tweet
        tweet_button_element.click()
        print("Complaint was tweeted.")

        # logout after sending the tweet
        # first open the account menu
        account_menu_button_element = self._wait_for_presence_of_element( 
                                    wait_time_sec=30,
                                    locator_strategy=By.CSS_SELECTOR,
                                    selector="div[data-testid='SideNav_AccountSwitcher_Button']",
                                    error_message="Error: Account menu.")
        if not account_menu_button_element: return False

        account_menu_button_element.click()

        # hit the logout button
        log_out_menu_button_element = self._wait_for_presence_of_element(
                                    wait_time_sec=30,
                                    locator_strategy=By.CSS_SELECTOR,
                                    selector="a[href='/logout']",
                                    error_message="Error: Account menu.")
        if not log_out_menu_button_element: return False

        log_out_menu_button_element.click()

        time.sleep(5)

        # bye bye twitter
        confirm_log_out_button_element = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
        confirm_log_out_button_element.click()

        time.sleep(3)
        # quit the driver
        self.driver.quit()