# class for handling kahoot
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class KahootHandlerBotSEttings:
    """
    settings for the kahoot bot 
    """
    # link to forms
    URL_TO_MY_Kahoot = "https://create.kahoot.it/creator"


class KahootHandlerBot:
    """
    with help of selenium handling the kahoot
    """
    def __init__(self, chrome_driver_path: str) -> None:
        # the path for the chrome driver
        self.chrome_driver_path = chrome_driver_path

    def _init_drivers(self) -> None:
        """
        Init drivers
        """
        #  creating service for the chrome driver
        self.chrome_driver_service = Service(self.chrome_driver_path)
        # creating the webdriver
        self.driver = webdriver.Chrome(service=self.chrome_driver_service)
        self.driver.maximize_window()

    def _open_website(self) -> None:
        """
        function to open the website
        """
        self.driver.get(KahootHandlerBotSEttings.URL_TO_MY_Kahoot)

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


    def _log_in(self, user_name: str, password: str) -> None:
        """
        loggin into the website
        """
        login_username = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.CSS_SELECTOR,
            selector='input[name="username"]',
            error_message="Cant find username on the login page!",
        )

        login_password = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.CSS_SELECTOR,
            selector='input[type="password"]',
            error_message="Cant find password on the login page!",
        )

        # filling data
        login_username.send_keys(user_name)
        time.sleep(1)
        login_password.send_keys(password)

        # login !
        login_password.send_keys(Keys.ENTER)

        # and entering the kabooth create page
        create_kahoot_button = self._wait_for_presence_of_element(
            wait_time_sec=10,
            locator_strategy=By.XPATH,
            selector='//*[@id="template-dialog"]/div/div[2]/div/div/button',
            error_message="Cant find create button after the login page!",
        )

        create_kahoot_button.send_keys(Keys.ENTER)

    def _add_question(self, question: str) -> None:
        """
        adding a question and answears
        """
        question_input = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.XPATH,
            selector='//*[@id="question-text-field"]/div/div[2]/div/div/div/div',
            error_message="Cant find question_input on the cretea page!",
        )

        answer_no_button = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.XPATH,
            selector='//*[@id="question-choice-0"]/div/div[2]/div/div',
            error_message="Cant find answer_no_button on the cretea page!",
        )
        
        answer_no_clue_button = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.XPATH,
            selector='//*[@id="question-choice-1"]/div/div[2]/div/div',
            error_message="Cant find answer_no_clue_button on the cretea page!",
        )

        answer_maybe_button = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.XPATH,
            selector='//*[@id="question-choice-2"]/div/div[2]/div/div',
            error_message="Cant find answer_maybe_button on the cretea page!",
        )

        answer_yes_button = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.XPATH,
            selector='//*[@id="question-choice-3"]/div/div[2]/div/div',
            error_message="Cant find answer_yes_button on the cretea page!",
        )

        # enetering the question and the answers
        question_input.send_keys(question)
        answer_no_button.send_keys('NO')
        answer_no_clue_button.send_keys("NO CLUE")
        answer_maybe_button.send_keys("MAYBE")
        answer_yes_button.send_keys("YES")



        select_correct_answer_no_clue = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.XPATH,
            selector='//*[@id="1"]',
            error_message="Cant find select_correct_answer_no_clue on the cretea page!",
        )
        
        # clicking the correct answear
        select_correct_answer_no_clue.click()


    def _create_another_question(self) -> None:
        """
        create another question
        """
        add_question_button = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.CSS_SELECTOR,
            selector='button[data-functional-selector="add-question-button"]',
            error_message="Cant find add_question_button!",
        )

        # adding another question
        add_question_button.click()

        create_button_quiz = self._wait_for_presence_of_element(
            wait_time_sec=5,
            locator_strategy=By.CSS_SELECTOR,
            selector='button[data-functional-selector="create-button__quiz"]',
            error_message="Cant find create_button_quiz!",
        )

        # adding another question
        create_button_quiz.click()


    def _change_question_time(self, time_option: int) -> None:
        """
        time_option:
        0 - 5sec,
        1 - 10sec,
        2 - 20sec,
        3 - 30 sec,
        4 - 1min
        5 - 1min30sec
        6 - 2min
        7 - 4min
        changing the question time to answer
        """
        time_option = int(time_option)
        if 0 <= time_option <= 7:
            open_time_drop_down = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.XPATH,
                selector='//*[@id="root"]/div/div/main/div/div[2]/div[1]/div[2]/label/div/div',
                error_message="Cant find open_time_drop_down!",
            )

            # open time drop down
            open_time_drop_down.click()

            # options 0-7
            select_time_option = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.CSS_SELECTOR,
                selector=f'div[id="react-select-3-option-{time_option}"]',
                error_message="Error: select_time_option",
            )

            # open time drop down
            select_time_option.click()
        else:
            print(f"{time_option} is not in range 0-7 and not an integer!!")

    def _save_survey(self, title: str, desc: str) -> None:
        """
        Saves the survey
        """
        time.sleep(3)
        save_button = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.CSS_SELECTOR,
                selector='button[data-functional-selector="top-bar__save-button"]',
                error_message="Error: save_button",
            )
        
        # hitting the save button
        save_button.click()

        # adding title and description
        title_input = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.CSS_SELECTOR,
                selector='input[data-functional-selector="dialog-information-kahoot__kahoot_title_input"]',
                error_message="Error: title_input",
            )

        textarea_input = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.CSS_SELECTOR,
                selector='textarea[data-functional-selector="dialog-information-kahoot__kahoot_description_textarea"]',
                error_message="Error: textarea_input",
            )


        title_input.send_keys(title)
        textarea_input.send_keys(desc)

        # confirm continue
        continue_button = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.CSS_SELECTOR,
                selector='button[data-functional-selector="dialog-add-title__continue"]',
                error_message="Error: continue_button",
            )
        
        continue_button.click()

        # confirming done !
        confirm_button = self._wait_for_presence_of_element(
                wait_time_sec=5,
                locator_strategy=By.CSS_SELECTOR,
                selector='button[data-functional-selector="dialog-complete-kahoot__finish-button"]',
                error_message="Error: confirm_button",
            )
        
        confirm_button.click()
        

    def do_kahoot(self, username: str, password: str, places: list[str], option_time:int, title:str, description: str) -> None:
        """
        creatign kahoot
        """
        self._init_drivers()

        self._open_website()
        time.sleep(1)
        self._log_in(username,password)
        time.sleep(2)

        for element in places:
            self._add_question(element)
            self._change_question_time(option_time)
            if not element == places[-1]:
                self._create_another_question()

        self._save_survey(title,description)

        print("data was saved to the kahoot!")
        time.sleep(20)

        #bey bey
        self.driver.quit()