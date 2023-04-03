import os

import spotipy
from spotipy import SpotifyOAuth

from dotenv import load_dotenv

load_dotenv()  # load environment variables
# permissions required from my spotify app to shuffle things
# see https://developer.spotify.com/documentation/web-api/concepts/scopes

SCOPES = "user-library-read " \
         "playlist-modify-private " \
         "playlist-modify-public " \
         "ugc-image-upload"
# "app-remote-control " \
# "streaming " \
# why doesn't python let you make consts, so dumb




# filepath to playlists.txt
# FILEPATH = 'playlists.txt'  # this only works in cmd
FILEPATH = 'src/playlists.txt'  # this only works in ide

AUTH = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                                 client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                                                 redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
                                                 scope=SCOPES))


def ask_int(query, low, high):
    while True:
        choice = input(query + "\n\n> ")
        try:
            choice = int(choice)
            if choice > high or choice < low:
                print("Please enter an integer between " + str(low) + " and " + str(high))
                continue
            return choice


        except ValueError:
            print("Please enter an integer between " + str(low) + " and " + str(high))
