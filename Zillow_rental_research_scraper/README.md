# Zillow_rental_research_scraper

This is a program that tackles a research data entry job where the aim is to
find house prices that fit a particular client's criteria. The house prices will be scrapped
using python's library Beautifulsoup from the Zillow website https://www.zillow.com/.
The address, price for rent, and link with the offer will be stored in a dictionary.
The program will then use Python's Selenium library to transfer that data into a Google form https://docs.google.com/forms/ (Auto filling the forms). After the process is done, the user can download or view the data in a Google spreadsheet. BeautifulSoup + Selenium.</br>

---

What is the aim of the program:</br>
1. We are going to go to Zillow, which is one of the largest real estate listing sites in the US, and we are going to search to see if we can find a place to rent in San Francisco.</br>
2. Clients' criteria (output should be a list with all the places that meet the criteria):</br>
- San Francisco, CA (area)</br>
- up to 3000 USD per month (max price)</br>
- at least 1 bedroom (at least one bedroom)</br>

---

The necessary steps to make the program work:</br>
1. Install the Chrome web browser https://www.google.com/intl/en_uk/chrome/ </br>
2. Download Chrome Driver (don't forget to match the version of your Chrome with the version of the Chrome Driver) https://chromedriver.chromium.org/downloads, and unzip the file for your OS.
Mark the DIR to the chromedriver.exe file and adjust the *CHROME_DRIVER_PATH* in main.py. </br>
3.  Set up a Gmail account, https://accounts.google.com/.  </br>
4. Make your own Google Form: Sign in to your Gmail account, then go to https://docs.google.com/forms/ and create a form:</br>  
- Step 1 - create a blank form:</br>
</br>

![Screenshot](docs/img/01_create_a_blank_form.png)</br>
</br>

- Step 2 - fill in the three questions as short answers as below:</br>
</br>

![Screenshot](docs/img/02_create_a_form_example.png)</br>
</br>

- Step 3 - copy the link to the form:</br>
</br>

![Screenshot](docs/img/03_create_a_link_to_form.png)</br>
</br>

5. The user has to adjust the starting variables in main.py:</br>
*CHROME_DRIVER_PATH* - as stated in point 2.</br>
6. The user has to adjust the starting variables in form_bot.py:</br>
*URL_TO_MY_FORM* - as stated in point 4 - step 3.</br>
7. The user has to adjust the starting variables in the web_scrapper.py:</br>
*MY_HTTP_HEADER* - go to http://myhttpheader.com/ to check your own header values and update them accordingly.</br>
*WEBSITE_URL_ZILLOW_PREDEFINED_SEARCH* - It is already pre-populated with an example URL. It is possible to adjust the search criteria by visiting the website https://www.zillow.com/ and selecting the criteria that we want, like location, max price, for rent or sale, in order to get a list of elements. After we are done, we have to copy the url which will include the searching criteria and define our variable as this url.</br>
</br>
An example view of a given search criteria for Zillow:</br>
</br>

![Screenshot](docs/img/04_zillow_website.png)
</br>

8. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>

---

**Creating a Google Spread Sheet after the forms are submitted.**</br>
Under the tab Responses, there is a button to view the response in sheets.. 
![Screenshot](docs/img/05_creating_google_spread_sheet.png)</br>

</br>

**An example view of the spreadsheet after the process is done.**</br>
![Screenshot](docs/img/06_google_spread_sheet_filled_done.png)</br>


---

**The program was developed using python 3.10.6, selenium, BeautifulSoup, requests**


In order to run the program, you have to execute main.py.