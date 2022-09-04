# Spotify_playlist_generator

This program validates the given date by the user with regular expression operations and later uses Python's BeautifulSoup library for scraping data from a music website ( https://www.billboard.com/charts/hot-100/ ) for that date, in order to find a list of top 100 songs. Based on the scraped data, it will automatically create a Spotify playlist using the spotipy library (Spotify API).

---

The program will be executed in the following steps:</br>
1. Awaiting user input: a date input in the format YYYY-MM-DD (like 2020-12-20), which will be validated using regular expression operations.</br>
![Screenshot](docs/img/01_user_input.png)
</br>
2. The date from step 1 will be used to scrape the data from the website https://www.billboard.com/charts/hot-100/  .</br>
3. The song titles will be retrieved from step 2 and converted into a list.</br>
4. A Spotify token will be created to authenticate your Python project with Spotify (user authorization with OAuth).</br>
5. The authorized user will use the app to retrieve URIs from sportify for each of the song titles from step 3.</br>
6. A Spotify playlist will be created and populated with the songs from step 5.</br>

---

*Main libraries used in this porgram:*</br> 

**BeautifulSoup**</br>
https://www.crummy.com/software/BeautifulSoup/bs4/doc/</br>

**re — Regular expression operations**</br>
https://docs.python.org/3/library/re.html</br>

**requests**</br>
https://requests.readthedocs.io/en/latest/</br>

**spotipy**</br>
https://spotipy.readthedocs.io/en/master/</br>


---

In order to run the program:</br>
1. Create a free Spotify account.
https://open.spotify.com/  , and login to your account.</br>
2. Login to the developer-Spotify https://developer.spotify.com/dashboard/ ,
and create an app, giving it a name and description (https://developer.spotify.com/documentation/general/guides/authorization/app-settings/).</br>
![Screenshot](docs/img/02_create_app.png)</br>
3. Obtain your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET and set the SPOTIPY_REDIRECT_URI (https://spotipy.readthedocs.io/en/master/)</br>
![Screenshot](docs/img/03_client_id_secret.png)</br>
![Screenshot](docs/img/04_adding_redirect_uris.png)</br>
4. Change the name of .env.example to .env and define the variables according to your data:</br>
SPOTIPY_CLIENT_ID="your-spotify-client-id" </br>
SPOTIPY_CLIENT_SECRET="your-spotify-client-secret" </br>
SPOTIPY_REDIRECT_URI='your-app-redirect-url' </br>
5. Run the file main.py and enter the date in the correct format.</br>
![Screenshot](docs/img/01_user_input.png)</br>
6. The end result should be the creation of a playlist in your account with the given date.</br>
![Screenshot](docs/img/05_created_playlist.png)</br>


---


**The program was developed using python 3.10.6, BeautifulSoup, requests, dotenv, re,  spotipy,  Spotify API.**


In order to run the program, you have to execute main.py.