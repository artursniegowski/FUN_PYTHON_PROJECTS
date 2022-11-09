# class handling the webscraping from zillow website
from bs4 import BeautifulSoup
import requests
import json

class ZillowScrapperSettings:
    """
    seettings for the Zillowscrapper
    """
    # this is the url from zillow with predefined search, 
    # location: San Francisco, CA
    # For Rent
    # max price: $3000
    # Bedrooms: 1+
    WEBSITE_URL_ZILLOW_PREDEFINED_SEARCH = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69125507932883%2C%22north%22%3A37.859232413339626%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

    # define your header
    # You'll need to pass along some headers in order for the request to return the actual website HTML
    # otherwise the website will think you are a bot/robot and will not allow the content
    # go to http://myhttpheader.com/ to check these values and update them accordingly. 
    MY_HTTP_HEADER = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Language":"en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,de;q=0.6,la;q=0.5,ar;q=0.4",
        "Connection":"close",
    }


class ZillowScrapper:
    """
    class for scrapping data from zillow website
    """
    def __init__(self, zillow_website_url: str, **kwargs) -> None:
        self.zillow_website_url = zillow_website_url
        self.response = requests.Response()
        self.soup = BeautifulSoup()
        self.headers = kwargs.get('headers', None)

        # init values
        self._get_raw_data()

    def _get_raw_data(self) -> None:
        """
        returns raw data from the given website,
        the response will be populated with that data. 
        the soup object will be poppulated with data

        The text() method of the Request interface reads the request body and 
        returns it as a promise that resolves with a String. 
        The response is always decoded using UTF-8.
        """
        self.response = requests.get(url=self.zillow_website_url,
                                    headers=self.headers)
        self.response.raise_for_status() # check for any errors
        # self.response.encoding = 'utf-8' # if not set

        #print(self.response.text)
        # getting bs4 / BeautifulSoup object
        # self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
    

    def return_zillow_listing(self) -> list[dict]:
        """
        return a dictionary with house listings 
        for each house it has price, address and href  keys defined
        """

        # this solution wont work, bc zillow website preloads the listing elemts dynamicaly with javascript
        # hence when we laod the website we will just get few results, like 9 and the rest will be empty.
        # to solve this either we have to open the website and scrole up and down to load the data listings
        # or we just tap into the script data after geting the data from request
        # listing_elements = self.soup.select(selector="div#search-page-list-container > div#grid-search-results > ul > li")

        # for listing_element in listing_elements:
        #     # getting the price, address and href
        #     # print(listing_element)
        #     try:
        #         price = listing_element.select_one(selector='span[data-test="property-card-price"]').get_text()
        #         listing_href = listing_element.select_one(selector='a[data-test="property-card-link"]')['href']
        #         if not 'www.zillow.com' in listing_href:
        #             listing_href = "https://www.zillow.com" + listing_href

        #         address = listing_element.select_one(selector='address[data-test="property-card-addr"]').get_text()
                
        #     except AttributeError as error_atribute:
        #         print(error_atribute)
        #         print("Element dosent exist!")

        #     else:
        #         print(price)
        #         print(listing_href)
        #         print(address)



        # The results are stored in <script> variable inside the page:

        listing_elements_as_list = []
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children
        # geting data with loading the script as json
        all_listings = json.loads(
            self.soup.select_one("script[data-zrr-shared-data-key]").contents[0].strip("!<>-")
        )

        # going through each of the results

        for house_listing in all_listings["cat1"]["searchResults"]["listResults"]:
            
            listing_href = house_listing['detailUrl']
            if not 'www.zillow.com' in listing_href:
                listing_href = "https://www.zillow.com" + listing_href
            
            address = house_listing["address"]

            # Listings with multiple properties have a different structure from 
            # listings with a single property only. 
            # listings with multiple properties have units list 
            if 'units' in house_listing:
                # multiple properties
                price = house_listing["units"][0]["price"]
            else:
                # single property
                price = house_listing["price"]
            price = price.strip(" +/mo")


            listing_elements_as_list.append({
                'address': address,
                'href': listing_href,
                'price': price,
            })

        return listing_elements_as_list

    

            