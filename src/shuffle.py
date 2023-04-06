import logging
import os
import sys

from pprint import pprint
from spotipy import SpotifyOAuth

from choose_playlist import choose_playlist
from new_playlist import copy_playlist_info
from getters import get_tracks, get_name_from_playlist_uri
from edit_playlists import add_tracks
from getters import PlaylistGetTypes
# from utils import auth
import utils
import random
# import logging
import spotipy
# import math
# from pprint import pprint
from edit_playlists import wipe_tracks_by_id


def shuffle_in_place():

    logger = logging.getLogger("shuffle()")
    logging.basicConfig(level="FATAL")  # else it'll display errors for invalid entries

    sp = utils.auth()


    playlist = choose_playlist("select playlist to shuffle:", only_editable=True)  # prompt user for source playlist
    if playlist == "CANCELLED":
        return  # cancel this function and go up a level


    # print("shuffle " + source_playlist)


    results = get_tracks(playlist_id=playlist, return_type=PlaylistGetTypes.IDS_ONLY, keep_local=True)
    # THIS WILL NOT RETURN THE IDS OF ANY LOCAL TRACKS

    ids = results[0]
    local = results[1]
    # print(name)
    print("shuffling items")
    random.shuffle(ids)
    # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle
    # print('\n"' + name + '" shuffled successfully!\n')
    size = len(ids)
    from random import randrange
    # sys.exit(2)
    if local > 0:  # if local tracks present
        print("local tracks found")
        print("clearing all non-local tracks")
        # pprint(ids)
        # input("wipe?")
        wipe_tracks_by_id(playlist_id=playlist, tracks_to_wipe=ids)


        # input("add shuffled?")
        print("adding shuffled tracks")
        add_tracks(ids, playlist)  # add tracks


        print("shuffling local tracks")
        for i in range(local):
            insert = randrange(size-1)  # takes the first local and moves it to a random spot
            # print(insert)

            sp.playlist_reorder_items(playlist, range_start=0, insert_before=insert)


    else:



        print("clearing playlist")
        sp.playlist_replace_items(playlist, [])  # test that you own playlist. Also wipes it

        print("adding shuffled tracks")
        add_tracks(ids, playlist)  # add tracks
        name = get_name_from_playlist_uri(playlist)
        print('\n"' + name + '" shuffled successfully\n')

    # try:
    #     print("clearing destination playlist")
    #     sp.playlist_replace_items(destination_playlist, [])  # test that you own playlist. Also wipes it
    #
    #     add_tracks(ids, destination_playlist)  # add tracks
    #     name = utils.get_name_from_playlist_uri(destination_playlist)
    #     print('\n"' + name + '" shuffled successfully\n')
    #
    # except spotipy.exceptions.SpotifyException:
    #     print("\nerror: you do not own this playlist and cannot shuffle it in place\n"
    #           "however, you can create a new shuffled playlist with it, if you want\n")

def shuffle_new():
    # sp = utils.auth()

    source_playlist = choose_playlist("select playlist to copy:", only_editable=False)  # prompt user for source playlist
    if source_playlist == "PLAYLISTS.TXT_IS_EMPTY" or source_playlist == "CANCELLED":
        return


    destination_playlist = copy_playlist_info(source_playlist)  # create destination playlist


    ids = get_tracks(playlist_id=source_playlist, return_type=PlaylistGetTypes.IDS_ONLY, keep_local=False)
    # pprint(ids)
    # sys.exit(5)
    print("shuffling items")
    random.shuffle(ids)
    # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle

    add_tracks(ids, destination_playlist)

    name = get_name_from_playlist_uri(destination_playlist)
    # print('\nnew shuffled playlist "' + name + '" created successfully\n')
    print('\n"' + name + '" created successfully\n')
