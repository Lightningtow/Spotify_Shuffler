import logging
import os
import sys

from spotipy import SpotifyOAuth

from choose_playlist import choose_playlist
from new_playlist import new_playlist
from get_add_tracks import add_tracks, get_tracks

from data import PlaylistGetTypes
from utils import auth
import random
# import logging
import spotipy
# import math
# from pprint import pprint

def shuffle_in_place():

    # logger = logging.getLogger('chooser')
    logging.basicConfig(level='FATAL')  # else it'll display errors for invalid entries

    sp = AUTH


    source_playlist = choose_playlist("select playlist to shuffle:", only_editable=True)  # prompt user for source playlist
    if source_playlist == "PLAYLISTS.TXT_IS_EMPTY" or source_playlist == "CANCELLED":
        return
    # print("shuffle " + source_playlist)


    destination_playlist = source_playlist

    ids = get_tracks(source_playlist, PlaylistGetTypes.IDS_ONLY)



    print("shuffling tracks")
    random.shuffle(ids)
    # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle


    try:
        print("clearing destination playlist")
        sp.playlist_replace_items(destination_playlist, [])  # test that you own playlist. Also wipes it

        add_tracks(ids, destination_playlist)  # add tracks
        print("\nplaylist shuffled successfully!\n")

    except spotipy.exceptions.SpotifyException:
        print("\nerror: you do not own this playlist and cannot shuffle it in place\n"
              "however, you can create a new shuffled playlist with it, if you want\n")

def shuffle_new():
    sp = AUTH

    source_playlist = choose_playlist("select playlist to shuffle:", only_editable=False)  # prompt user for source playlist
    if source_playlist == "PLAYLISTS.TXT_IS_EMPTY" or source_playlist == "CANCELLED":
        return


    destination_playlist = new_playlist(source_playlist)  # create destination playlist


    ids = get_tracks(source_playlist, PlaylistGetTypes.IDS_ONLY)


    print("shuffling tracks")
    random.shuffle(ids)
    # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle

    add_tracks(ids, destination_playlist)
    print("\nnew shuffled playlist created successfully!\n")


#
# def old_shuffle(shuffle_type):
#
#     # logger = logging.getLogger('shuffle')
#     # logging.basicConfig(level='DEBUG')
#
#     sp = AUTH
#
#
#     source_playlist = choose_playlist("select playlist to shuffle:")  # prompt user for source playlist
#     if source_playlist == "PLAYLISTS.TXT_IS_EMPTY" or source_playlist == "CANCELLED":
#         return
#     # print("shuffle " + source_playlist)
#
#     destination_playlist = ""
#     if shuffle_type == "NEW":
#         destination_playlist = new_playlist(source_playlist)  # create destination playlist
#     elif shuffle_type == "IN_PLACE":
#         destination_playlist = source_playlist
#     else:
#         print("error in shuffle(): invalid shuffle type")
#         sys.exit(-1)
#
#
#     alltracks = get_tracks(source_playlist)
#
#     ids = []
#
#     for item in alltracks:  # scrub alltracks and convert to list of just ids
#         # print(item['track']['name'])
#
#         if item['is_local']:
#             print("    removing local track")  # lol doesn't actually remove from alltracks, just doesn't add to ids
#
#         elif item['track']['type'] == 'episode':
#             print("    removing podcast")
#
#         elif item['track']['id'] is not None:
#
#             ids.append(item['track']['id'])
#
#
#     print("shuffling tracks")
#     random.shuffle(ids)
#     # https://stackoverflow.com/questions/3062741/maximal-length-of-list-to-shuffle-with-python-random-shuffle
#
#
#     if shuffle_type == ShuffleType.NEW:  # NEW guarantees having a clean, editable playlist, so less precautions necessary
#         add_tracks(ids, destination_playlist)
#         print("\nnew shuffled playlist created successfully!\n")
#
#
#     elif shuffle_type == ShuffleType.IN_PLACE:
#         try:
#             print("clearing destination playlist")
#             sp.playlist_replace_items(destination_playlist, [])  # test that you own playlist. Also wipes it
#
#             add_tracks(ids, destination_playlist)  # add tracks
#             print("\nplaylist shuffled successfully!\n")
#
#         except spotipy.exceptions.SpotifyException:
#             print("\nerror: you do not own this playlist and cannot shuffle it in place\n"
#                   "however, you can create a new shuffled playlist with it, if you want\n")
#
#     else:
#         print("bug in program, please report. Reason: invalid switchcase for shuffle_type in shuffle()")
#         sys.exit(-1)
#
