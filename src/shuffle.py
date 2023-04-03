import os

from spotipy import SpotifyOAuth

from choose_playlist import choose_playlist
from new_playlist import new_playlist
from tracks import add_tracks, get_tracks

from data import AUTH

import random
# import logging
import spotipy
# import math
# from pprint import pprint

def shuffle():

    # logger = logging.getLogger('shuffle')
    # logging.basicConfig(level='DEBUG')

    sp = AUTH

    source_playlist = choose_playlist("select playlist to shuffle:")  # prompt user for source playlist
    if source_playlist == "PLAYLISTS.TXT_IS_EMPTY" or source_playlist == "CANCELLED":
        return
    # print("shuffle " + source_playlist)
    destination_playlist = new_playlist(source_playlist)  # create destination playlist



    alltracks = get_tracks(source_playlist)

    ids = []
    i = 0  # just for counting how many tracks are local

    for item in alltracks:  # scrub alltracks and convert to list of just ids
        # print(item['track']['name'])

        if item['is_local']:
            # alltracks.remove(item)  # apparently this just removes the next item instead of this one
            i += 1
            print("    removing local track")

        elif item['track']['type'] == 'episode':
            # alltracks.remove(item)  # same problem here
            i += 1
            print("    removing podcast")

        elif item['track']['id'] is not None:
            # print(item['track']['id'])
            # print("ADDING " + item['track']['name'])
            ids.append(item['track']['id'])


    print("shuffling tracks")
    random.shuffle(ids)


    add_tracks(ids, destination_playlist)  # add tracks
    print("new shuffled playlist created successfully!\n")
