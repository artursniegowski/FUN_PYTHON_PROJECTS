# class for handling filling in the form
from selenium import webdriver
from selenium.common.exceptions import  ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class FormHandlerBotSEttings:
    """
    settings for the FormHandlerBot
    """
    # link to forms
    URL_TO_MY_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSd10CiVPtgtcLDpABUKjYCzGnre43mEhKZWJKGXxZxErYigRg/viewform?usp=sf_link"


class FormHandlerBot:
    """
    with help of selenium handling the google forms 
    """
    def __init__(self, chrome_driver_path: str) -> None:
        #  creating service for the chrome driver
        self.chrome_driver_service = Service(chrome_driver_path)
        # creating the webdriver
        self.driver = webdriver.Chrome(service=self.chrome_driver_service)


    def _wait_for_presence_of_element(self, wait_time_sec: int, locator_strategy: By, 
        selector: str, error_message: str) -> WebElement :
        """
        function to wait for an element presence, and then returns this element
        if not found in a given time a Timeout exception will occure and the function will close the driver and 
        raise a TimeoutException
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
            raise TimeoutException



    def _open_form(self) -> None:
        """
        function to open the form
        """
        self.driver.get(FormHandlerBotSEttings.URL_TO_MY_FORM)


    def _write_data(self, house_listing: dict) -> None:
        """
        write the data of the dictionary into the form
        example how the dictionary has to look
                {
                'address': address,
                'href': listing_href,
                'price': price,
            }
        """
        # get the arguments if defined, otherwsie none
        address = house_listing.get('address',"None")
        href = house_listing.get('href',"None")
        price = house_listing.get('price',"None")

        # selecting the input elemets
        address_input_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.XPATH,
            selector="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]//input",
            error_message="Cant find address input element!"
        )

        # selecting the input elemets
        price_input_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.XPATH,
            selector="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]//input",
            error_message="Cant find price input element!"
        )

        # selecting the input elemets
        href_input_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.XPATH,
            selector="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]//input",
            error_message="Cant find www/href input element!"
        )

        # filling in data
        address_input_element.send_keys(address)
        price_input_element.send_keys(price)
        href_input_element.send_keys(href)

        # submiting data
        # selecting the button element
        button_submit_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.XPATH,
            selector="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div",
            error_message="Cant find submit button element!"
        )
    
        button_submit_element.click()

        # submitting another form
        # submiting another response
        button_submit_another_response_element = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.XPATH,
            selector="/html/body/div[1]/div[2]/div[1]/div/div[4]/a",
            error_message="Cant find submit button element!"
        )
        button_submit_another_response_element.click()




    def fill_in_data(self, house_data_listings: list[dict]) -> None:
        """
        fill in data in the form with the given list of dictionaries, 
        the dictionary has to be a list of dict
        example how the dictionary has to look
                {
                'address': address,
                'href': listing_href,
                'price': price,
            }
        """

        self._open_form()

        for element in house_data_listings:
            self._write_data(element)
 

        print("data was saved to the form. Well done! Success!")
        time.sleep(5)

        #bey bey
        self.driver.quit()