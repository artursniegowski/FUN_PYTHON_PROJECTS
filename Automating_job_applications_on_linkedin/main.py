from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# user defined email and app password for your linkedin account !
# env variables ! - dont change here !
MY_LINKEDIN_EMAIL = os.environ.get('MY_LINKEDIN_EMAIL')
MY_LINKEDIN_PASSWORD = os.environ.get('MY_LINKEDIN_PASSWORD')
PHONE_NUMBER = "555555555" # user defined number
################################################################################


####################### SELENIUM SETTINGS #########################
# adjust this path to wherever you have unpacked the chrome driver file !
# dont forget that the verion of chrom drive has to match the verison of chrome browser
# https://chromedriver.chromium.org/downloads
# relative path you can use as well absolute path !
chrome_driver_path = "ChromeDriver/chromedriver.exe"

# creating the webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# website url for the linkin job search with eaasy to apply status
# exampel url for web developer search
WEBSITE_URL_FOR_THE_DRIVER = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=web%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)

###### login in to linked in account - after accesing the website #####
login_button_element = driver.find_element(By.XPATH,'/html/body/div[3]/header/nav/div/a[2]')
login_button_element.click()

# wait for the page to load
time.sleep(5)

################### log in pag - login with the user credentials ############
login_email_input_element = driver.find_element(By.NAME, 'session_key')
login_email_input_element.send_keys(MY_LINKEDIN_EMAIL)

login_password_input_element = driver.find_element(By.NAME, 'session_password')
login_password_input_element.send_keys(MY_LINKEDIN_PASSWORD)
login_password_input_element.send_keys(Keys.ENTER)

# wait for the page to load
time.sleep(5)

# getting all the jobs from the one page
# jobs_list_elements = driver.find_elements(By.CSS_SELECTOR,'.job-card-container--clickable')
jobs_list_elements = driver.find_elements(By.CSS_SELECTOR,'div.job-card-container--clickable')

print(len(jobs_list_elements))
# selecting job by job card
for job_element in jobs_list_elements:
    # selectic the job card
    job_element.click()

    # wait for the page to load
    time.sleep(1)

    try:
        # hit the easy apply button
        easy_apply_button_element = driver.find_element(By.CSS_SELECTOR, 'div.jobs-apply-button--top-card button')
        easy_apply_button_element.click()

        # wait for the page to load
        time.sleep(2)

        # input phone number and continue
        phone_input_element = driver.find_element(By.CLASS_NAME,'fb-single-line-text__input')
        if phone_input_element.text == "": # if empty write down the phone number
            phone_input_element.send_keys(PHONE_NUMBER)

        # getting the submit button
        submit_button_element = driver.find_element(By.CSS_SELECTOR,'footer button')

        # checking if this is the right button
        # we are discarding multi step applications
        # only submit will be accepted
        if submit_button_element.get_attribute('aria-label') == 'Submit application':
            # submitting our application
            submit_button_element.click()
            
            # wait for the page to load
            time.sleep(3)

            # close the confirmation of submiting application
            close_application_element = driver.find_element(By.CLASS_NAME,'artdeco-modal__dismiss')
            close_application_element.click()

            # wait for the page to load
            time.sleep(2)

        else:
            # if the button is next we will close the appliction
            close_application_element = driver.find_element(By.CLASS_NAME,'artdeco-modal__dismiss')
            close_application_element.click()
            # wait for the page to load
            time.sleep(2)

            # pressing the discard button
            discard_application_element = driver.find_element(By.CLASS_NAME,'artdeco-modal__confirm-dialog-btn')
            discard_application_element.click()
            # wait for the page to load
            time.sleep(2)

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

print("done")
# close the browser
driver.quit() # this will close the whole browser