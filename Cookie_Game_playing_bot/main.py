# selenium bot playing the game
# https://orteil.dashnet.org/cookieclicker/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# USER DEFINED VARAIBLES
# amount of time for the game to play
TIMEOUT_GAME = time.time() + 60*10   # 5 minutes from now
# Time in seconds to check for new upgrades
TIME_FOR_UPGRADE = 10
# init value
CHECK_FOR_UPGRADE = time.time() + TIME_FOR_UPGRADE


####################### SELENIUM SETTINGS #########################
# adjust this path to wherever you have unpacked the chrome driver file !
# dont forget that the verion of chrom drive has to match the verison of chrome browser
# https://chromedriver.chromium.org/downloads
# relative path you can use as well absolute path !
chrome_driver_path = "ChromeDriver 104.0.5112.79 (2022-08-03)/chromedriver.exe"

# creating the webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# website where the game lives
WEBSITE_URL_FOR_THE_DRIVER = "http://orteil.dashnet.org/experiments/cookie/"
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################


############# CHOOSING THE ELEMENTS FOR THE GAME #########################
# select the cookie
cookie_element = driver.find_element(By.ID, "cookie")
# select the element showing the money
current_money_element = driver.find_element(By.ID, "money")
# getting upgrades items ids
store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
sore_elements_ids = [element.get_attribute("id") for element in store_elements]
# print(sore_elements_ids)
# for element_id in sore_elements_ids:
#     # check if the index 1 exists !
#     print(driver.find_element(By.ID,element_id).find_element(By.CSS_SELECTOR,"b").text.strip().split("-")[1].replace(',',''))

####################################################################


####################### main game loop #######################

while True:
    # checking if the time for playing the game is up
    # and if so break the loop
    if time.time() > TIMEOUT_GAME:
        # if game is over, print the cookies per second to console
        cookies_per_second_element = driver.find_element(By.ID,"cps")
        print(cookies_per_second_element.text)
        
        # break the main loop // end game
        break
    
    # check for upgrade every 5 seconds
    # buy the most expensive
    if time.time() > CHECK_FOR_UPGRADE: 
        
        # getting the value of cuurent money
        current_money =  int(current_money_element.text.replace(',',''))

        element_to_buy = None
        # check all element from the store if we can buy one
        # looking for the most expensive one 
        for store_element_id in sore_elements_ids:
            # checkig if we can afford to buy the upgrade
            checking_element_to_buy = driver.find_element(By.ID,store_element_id)
            
            # if we actually find an element check its price
            # check only visible elements ! 
            upgrade_data = checking_element_to_buy.find_element(By.CSS_SELECTOR,"b").text.split("-")
            if len(upgrade_data) > 1:
                # getting the price of the upgrade
                upgrade_pice = int(upgrade_data[1].strip().replace(',',''))

                # checking if we have enoug money to buy that upgrade
                if upgrade_pice < current_money:
                    element_to_buy = checking_element_to_buy
                # if we dont have money for the next element that break the search
                # bc the elments are in ascending order (in price)
                else:
                    break
        
        # buy the upgade we can afford if we actually found one
        if element_to_buy:
            element_to_buy.click()

        # every time we buy an upgrade we will wait longer with the next one
        TIME_FOR_UPGRADE *= 1.1
        # reset time - check for upgrade
        CHECK_FOR_UPGRADE = time.time() + TIME_FOR_UPGRADE
    
    
    # keep hitting the cookie
    cookie_element.click()



# close the browser
driver.quit() # this will close the whole browser
# driver.close() # this will close only the tab you have opened, one tab