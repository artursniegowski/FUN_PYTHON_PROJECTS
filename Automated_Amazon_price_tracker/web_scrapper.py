# class for scraping data
from bs4 import BeautifulSoup
import requests
import lxml

class AmazonScrapper:
    def __init__(self, product_website_url: str, **kwargs) -> None:
        self.product_website_url = product_website_url
        self.response = requests.Response()
        self.soup = BeautifulSoup()
        self.headers = kwargs.get('headers', None)

        # init values
        self._get_raw_data_from_website()

    def _get_raw_data_from_website(self) -> None:
        """
        returns raw data from the given website,
        the response will be populated with that data. 
        the soup object will be poppulated with data

        The text() method of the Request interface reads the request body and 
        returns it as a promise that resolves with a String. 
        The response is always decoded using UTF-8.

        """
        self.response = requests.get(url= self.product_website_url,
                                    headers=self.headers)
        self.response.raise_for_status() # check for any errors
        # # in case of encoding problems - if the encoding cant be resolved from the request
        # self.response.encoding = 'utf-8'

        # print(self.response.text)
        # getting bs4 / BeautifulSoup object
        # self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.soup = BeautifulSoup(self.response.text, "lxml")


    def return_the_price_of_product(self) -> float :
        """
        return the price of the product as an float object, if found
        otherwise returns None

        """
        price_element = self.soup.select_one(selector="div#corePrice_feature_div div.a-section span.a-price span.a-offscreen")
        
        if price_element:
            price = price_element.get_text().strip()
            try:
                price = float(price.split("$")[1])
                # price = float(price[1:])
            except SyntaxError:
                print(f"{price} : Issue with casting to float !!")
            else:
                return price

        return None


    def return_the_title_of_product(self) -> str:
        """
        returns the title of the product, if it cant fidn it,
        it will return empty string
        """
        
        title_element = self.soup.select_one(selector="div#titleSection h1#title span#productTitle")
        
        if title_element:
            title = title_element.get_text().strip()
            
            return title

        return ""