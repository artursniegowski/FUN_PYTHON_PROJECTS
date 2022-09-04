# class for scraping data
from bs4 import BeautifulSoup
import requests


class MusicScrapper:
    def __init__(self, website_base_url: str) -> None:
        self.website_base_url = website_base_url
        self.response = requests.Response()
        self.soup = BeautifulSoup()

    def get_raw_data_from_website(self, desired_date: str = "2020-10-10") -> None:
        """
        returns raw data from the given website,
        the response will be populated with that data. 


        The text() method of the Request interface reads the request body and 
        returns it as a promise that resolves with a String. 
        The response is always decoded using UTF-8.

        desired_date is a string in format YYYY-MM-DD
        """
        self.response = requests.get(self.website_base_url+desired_date)
        self.response.raise_for_status() # check for any errors
        # # in case of encoding problems - if the encoding cant be resolved from the request
        # self.response.encoding = 'utf-8'

        self._create_soup_object()

    def _create_soup_object(self) -> None:
        # getting bs4 / BeautifulSoup object
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def return_list_of_100_songs(self) -> list[str] :
        """
        return a list of 100 songs from the soup object
        """
        # using the css selector
        # soup.find_all(name='h3', id=title-of-a-story, class_='title') - different aproaches 

        song_titles = self.soup.select(selector=".o-chart-results-list__item h3#title-of-a-story")
        if song_titles:
            return [str(song_title.get_text()).strip() for song_title in song_titles]
        
        # if no song titles found return empty  list
        return []