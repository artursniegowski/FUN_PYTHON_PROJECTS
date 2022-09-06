# main program
import re
from web_scrapper import MusicScrapper

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

# spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# const defined
USER_MESSAGE_TIME_TRAVEL = "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
MUSIC_WEBSITE_BASE_URL = "https://www.billboard.com/charts/hot-100/"

# Spotify
SPOTIPY_SCOPE = "playlist-modify-private"
################################################################################
## sensitive data ###
#####################
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
################################################################################


# function for validating the input date - if it is in the right format
def check_if_date_is_valid(input_date: str) -> bool:
    """
    returns true if the input_date is in format YYYY-MM-DD,
    otherwise returns false
    """
    if re.search("^(\d{4})-\d{2}-(\d{2})$", input_date):
        return True
    else:
        return False


# user interaction - geting the specific date
# and checking for the right format
while True:
    user_defined_date = input(USER_MESSAGE_TIME_TRAVEL)
    user_defined_date = user_defined_date.strip()

    if check_if_date_is_valid(user_defined_date):
        break
    else:
        print(f"{user_defined_date} is not in the format YYYY-MM-DD like 2020-10-10. Please try again.\n")


########################################
# scraping the data from billboard.com #
########################################
# creatign an object for scrapign data
music_scraper = MusicScrapper(MUSIC_WEBSITE_BASE_URL)
# adding the requested date
music_scraper.get_raw_data_from_website(user_defined_date)
# getting a list of the 100 songs from that date
song_list = music_scraper.return_list_of_100_songs()

# print(song_list)

###########################
# Authorizing spotify app #
###########################
# spotify with spotipy
# you dont need to pass SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
# but you have to set them as env variables !
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                    client_id=SPOTIPY_CLIENT_ID,
                                                    client_secret=SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri=SPOTIPY_REDIRECT_URI,
                                                    scope=SPOTIPY_SCOPE,
                                                    # If true, a login prompt always shows (optional, defaults to False)
                                                    show_dialog = True,
                                                    # # path to location to save tokens (optional)
                                                    cache_path="token.txt",
                                                    ))
user_id = spotify.current_user()['id']
# print(user_id)

# retrieving the year in which the song appeared
year_to_search = user_defined_date.split('-')[0]


####################################
# Getting songs uris from sppotify #
####################################
list_spotify_song_uris = []
for track_name in song_list:
    results = spotify.search(q=f'track:{track_name} year:{year_to_search}', limit=1, type='track')

    try:
        # spotify_uri = 'spotify:track:6rqhFgbbKwnb9MLmUQDhG6'
        # print(results['tracks']['items'][0]['uri'])
        spotify_song_uri = results['tracks']['items'][0]['uri']
    except (KeyError, IndexError) : # in case of empty dictionary or non exisitng item in the list
        print(f"{track_name} did not match any results! It wont be included in the list.")
    else:
        list_spotify_song_uris.append(spotify_song_uri)


# print(list_spotify_song_uris)

#####################################################
# Create a playlist and adding the songs URIs to it #
#####################################################
desc_message = "Best of"
play_list = spotify.user_playlist_create(
                                        user=user_id, 
                                        name=f"{user_defined_date} Billboard 100", 
                                        public=False, 
                                        description="{} {}".format(desc_message, user_defined_date))

# print(play_list)
play_list_id = play_list['id']
# print(play_list_id)

# adding the songs URIs to the playlist
spotify.playlist_add_items(
                            playlist_id=play_list_id,
                            items=list_spotify_song_uris)

print(f"You have created playlist with id {play_list_id}")