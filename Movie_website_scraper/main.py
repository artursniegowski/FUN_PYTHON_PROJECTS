from bs4 import BeautifulSoup
import requests

WEBSITE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
FILE_NAME = 'movies.txt'


response = requests.get(WEBSITE_URL)
response.raise_for_status() # checking for errors
# The server is not sending the appropriate header, requests doesn't parse 
# <meta charset="utf-8" />, so it defaults to ISO-8859-1.
# SOLUTION:
# 1. setting to response.encoding = utf-8
# 2. html_text = r.content.decode('utf-8') - doing encoding yourself
# 3. Have requests take a guess r.encoding = r.apparent_encoding
response.encoding = 'utf-8'#response.apparent_encoding


# getting bs4 / BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# using the html tag and class selector
#movie_titles = soup.find_all(name='h3', class_='title')
# using the css selector
movie_titles = soup.select(selector='h3.title')


# careting the list of movesi and reversing the order
# list_of_movies = [movie.string + '\n' for movie in movie_titles][::-1] 
list_of_movies = [movie.string + '\n' for movie in movie_titles][::-1] 


# saving the list to a txt file
with open(FILE_NAME, 'w', encoding='utf-8') as f:
    f.writelines(list_of_movies)
