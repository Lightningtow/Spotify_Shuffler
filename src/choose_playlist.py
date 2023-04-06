import logging

from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth
# from data import SCOPES, FILEPATH, AUTH
from getters import get_all_playlists_from_user
from utils import ask_int


def choose_playlist(query, only_editable):
    # shows a list of all playlists and asks the user to choose one
    # parameters:
    #   query: a string for what to ask the user (remove, shuffle etc)
    #   only_editable: a bool for whether it should only display playlists that the user has the right to remove
    # called by shuffle() to determine which playlist to shuffle, and by remove_playlist to figure what to remove
    # return values:
    # either returns a playlist uri, or "CANCELLED" if the user cancels
    # returns a playlist id from all the playlists the user has

    # logger = logging.getLogger('chooser')
    logging.basicConfig(level='FATAL')  # else it'll display errors for invalid entries


    pdict = get_all_playlists_from_user(get_only_editable=only_editable, return_count="ALL")  # get all playlist info and stick it in a giant dict
        # pprint(y)
    # print(playlistdict.items())
    i = 0
    for name in pdict:  # iterate through all returned playlists
        i += 1
        print("<" + str(i) + "> " + name)  # pdict[name] to get value

    print("\n<0> cancel")

    # query = "\n" + query_arg  # quary is passed as argument lol

    # pprint(pdict.values()[3])
    names = list(pdict.keys())
    ids = list(pdict.values())

    choice = ask_int(('\n' + query), 0, i) - 1

    # print(str(ids[choice]) + " - " + names[choice])

    if choice == -1:
        return "CANCELLED"

    # print("returning " + ids[choice])
    return ids[choice]
