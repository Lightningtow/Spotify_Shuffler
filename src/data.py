import os
import spotipy
from spotipy import SpotifyOAuth
from dotenv import load_dotenv
from enum import Enum

load_dotenv()  # load environment variables
# permissions required from my spotify app to shuffle things, see https://developer.spotify.com/documentation/web-api/concepts/scopes
# put a space after the scope or it wont work
SCOPES = "user-library-read " \
         "playlist-modify-private " \
         "playlist-modify-public " \
         "ugc-image-upload " \
         "streaming " \
         "app-remote-control " \
         "playlist-read-private " \
         "playlist-read-collaborative "


class PlaylistGetTypes(Enum):
    FULLDATA = 1
    IDS_ONLY = 2

# class AuthReturnValues(Enum):

# class PlaylistEditability(Enum):
#     ALL = 1
#     ONLY_EDITABLE = 2

# "streaming " \
# why doesn't python let you make consts, so dumb


# filepath to playlists.txt
# FILEPATH = 'playlists.txt'  # this only works in cmd
FILEPATH = 'src/playlists.txt'  # this only works in ide

# AUTH = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
#                                                  client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
#                                                  redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
#                                                  scope=SCOPES))
