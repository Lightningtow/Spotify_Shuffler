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


def shuffle_in_place(uid_to_shuffle = "DEFAULT"):
    if uid_to_shuffle == "DEFAULT":
        print("error: no argument passed to shuffle_in_place")
        exit(-1)
    try:
        get_name_from_playlist_uri(uid_to_shuffle)
    except spotipy.exceptions.SpotifyException:
        print("error: invalid uid passed to shuffle_in_place")
        exit(-1)

    logger = logging.getLogger("shuffle()")
    logging.basicConfig(level="FATAL")  # else it'll display errors for invalid entries

    sp = utils.auth()


    playlist = uid_to_shuffle
    # playlist = choose_playlist("select playlist to shuffle:", only_editable=True)  # prompt user for source playlist
    # if playlist == "CANCELLED":
    #     return  # cancel this function and go up a level


    # print("shuffle " + source_playlist)


    results = get_tracks(playlist_id=playlist, return_type=PlaylistGetTypes.IDS_ONLY, return_local=False)
    # THIS WILL NOT RETURN THE IDS OF ANY LOCAL TRACKS

    ids = results[0]
    local = results[1]
    # pprint(results)
    print("shuffling items")
    random.shuffle(ids)
    # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle
    # print('\n"' + name + '" shuffled successfully!\n')
    size = len(ids)
    from random import randrange
    # sys.exit(2)
    keeping = "lol"
    if local > 0:
        print("local tracks found")
        while True:  # todo fix read logic here
            # print("keep local tracks? y/n\n"
            #       "if you do, you may have to re-download part of your playlist\n"
            #       "see README for details")
            # yn = input("> ")
            yn = "y"  # todo remove bypass when ready

            # print(">" + yn + "<")
            if yn == "y" or yn == "Y":
                keeping = True
                break
            elif yn == "n" or yn == "N":
                keeping = False
                break
            else:
                print("invalid input")
        # if local > 0:  # if local tracks present

        if keeping:
            print("clearing all non-local tracks")
            # pprint(ids)
            # input("wipe?")
            wipe_tracks_by_id(playlist_id=playlist, tracks_to_wipe=ids)

            # input("add shuffled?")
            print("adding shuffled tracks")
            add_tracks(ids, playlist)  # add tracks

            print("shuffling local tracks")
            for i in range(local):
                insert = randrange(size - 1)  # takes the first local and moves it to a random spot
                # print(insert)

                sp.playlist_reorder_items(playlist, range_start=0, insert_before=insert)

            name = get_name_from_playlist_uri(playlist)
            print('\n"' + name + '" shuffled successfully\n')
            return
        # elif not keeping:


    # this runs if no local tracks, or if local but not keeping
    print("clearing playlist")
    sp.playlist_replace_items(playlist, [])  # test that you own playlist. Also wipes it

    print("adding shuffled tracks")
    add_tracks(ids, playlist)  # add tracks
    name = get_name_from_playlist_uri(playlist)
    print('\n"' + name + '" shuffled successfully\n')

        # else:
        #     print("error, invalid value for 'keeping' in shuffle.py")
        #     exit(-1)




    # else:

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

def shuffle_new(uid_to_shuffle = "DEFAULT"):
    if uid_to_shuffle == "DEFAULT":
        print("error: no argument passed to shuffle_new")
        exit(-1)
    try:
        get_name_from_playlist_uri(uid_to_shuffle)
    except spotipy.exceptions.SpotifyException:
        print("error: invalid uid passed to shuffle_new")
        exit(-1)

    # sp = utils.auth()
    # print(uid_to_shuffle)

    source_playlist = uid_to_shuffle

    # source_playlist = choose_playlist("select playlist to copy:", only_editable=False)  # prompt user for source playlist
    # if source_playlist == "PLAYLISTS.TXT_IS_EMPTY" or source_playlist == "CANCELLED":
    #     return


    destination_playlist = copy_playlist_info(source_playlist)  # create destination playlist


    results = get_tracks(playlist_id=source_playlist, return_type=PlaylistGetTypes.IDS_ONLY, return_local=False)
    ids = results[0]
    # pprint(ids)
    # sys.exit(5)
    # print("result", type(result))
    #
    # print("results:")
    # pprint(result)
    # removed_tracks: int = result[0]
    #
    # ids: list = result
    # del ids[0]
    # pprint(ids)

    # print(removed_tracks)
    print("shuffling items")
    random.shuffle(ids)
    # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle

    add_tracks(ids, destination_playlist)

    name = get_name_from_playlist_uri(destination_playlist)
    # print('\nnew shuffled playlist "' + name + '" created successfully\n')
    print('\n"' + name + '" created successfully\n')
