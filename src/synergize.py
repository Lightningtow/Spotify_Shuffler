import math
from pprint import pprint
from time import sleep

import spotipy

from src import utils
from src.edit_playlists import add_tracks
from src.getters import get_diff, PlaylistGetTypes, get_name_from_playlist_uri, get_tracks, get_queue
from src.purge import use_purgelist
from src.utils import auth


def remove_dupes(playlist_uid="DEFAULT"):
    if playlist_uid == "DEFAULT":
        print("error: no argument passed to shuffle_new")
    try:
        get_name_from_playlist_uri(playlist_uid)
    except spotipy.exceptions.SpotifyException:
        print("error: invalid uid passed to shuffle_new")
        exit(-1)

    sp = auth()

    playlist_uid = utils.AFTERPURGE  # roadkill test
    results = get_tracks(playlist_id=playlist_uid, return_type=PlaylistGetTypes.IDS_ONLY, return_local=False)
    ids = results[0]
    readlist = []
    pos = -1  # so it starts at 0
    remove_me = []
    hundreds = 0
    biglist = []

    dupes = 0
    for item in ids:
        pos += 1

        if item not in readlist:
            readlist.append(item)
            # print("appending", item)
        elif item in readlist:
            dupes += 1

            chunk = {"uri": item, "positions": [pos]}
            chunklist = [chunk]
            # print(type(chunklist))

            # sp.playlist_remove_specific_occurrences_of_items(playlist_uid, chunklist)

            remove_me.append(chunk)
            if len(remove_me) == 100:
                # remove_me = remove_me.json()
                biglist.append(remove_me)
                remove_me = []
                pos = pos - 100  # else its screwed when you remove in multiple chunks
    if len(remove_me) > 0:
        biglist.append(remove_me)
    # sp.playlist_remove_specific_occurrences_of_items(playlist_uid, remove_me)

    # size = len(ids)
    # hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    # leftovers = size - (hundreds * 100)  # number of tracks to add for the last non-100 chunk

    sp = auth()

    # pprint(biglist, sort_dicts=False)
    # print("len", len(biglist))
    # for item in biglist:
    #     print("wow", len(item))
    print("found", dupes, "duplicates")
    # newlist = []

    # if size > 100:
    #     print("removing " + str(size) + " items")
    #
    #     for i in range(hundreds):
    #         newlist = ids[i * 100:(i + 1) * 100]  # make list of tracks to remove this cycle
    #
    #         print("\tremoving items " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
    #
    #         sp.playlist_remove_all_occurrences_of_items(playlist_id, newlist)
    #
    #         # print("successfully added tracks " + str((i * 100)+1) + " - " + str((i + 1)*100))
    #
    #
    # print("\tremoving items " + str((hundreds * 100) + 1) + " - " + str((hundreds * 100) + leftovers))
    # newlist = ids[-leftovers:]  # make list of leftover songs
    # sp.playlist_remove_all_occurrences_of_items(playlist_id, newlist)

    for innerlist in biglist:
        print("removing:")
        pprint(innerlist, sort_dicts=False)
        snapshot_id = sp.playlist_remove_specific_occurrences_of_items(playlist_uid, innerlist)
        # for i in range(10):
        print("snapshot id:", snapshot_id)

    # todo crashes on local tracks
    # least it works for podcasts


def current_func():
    sp = auth()
    # fulldata = sp.devices()
    # pprint(fulldata)
    # sp.pause_playback()
    # get_queue()
    sp.start_playback(device_id=None, context_uri="spotify:track:2xZlBSmWu87B5Os7eQL7LL")

# def current_func():
#     sp = auth()
#     # fulldata = sp.current_playback()
#     # fulldata['item']['album']['available_markets'] = ""
#     # fulldata['item']['available_markets'] = ""
#
#     fancylist = []
#     fulldata = sp.current_user_top_tracks(time_range='short_term')
#     # pprint(fulldata)
#     for i in range (20):  # using list1 doesn't work
#
#     # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
#         entry = fulldata['items'][i]['artists'][0]['name']   + " - " + fulldata['items'][i]['name']
#         #   + " - " + fulldata[i]['track']['album']['name']
#         fancylist.append(entry)
#     pprint(fancylist)
#     print("=============================================")
#     fancylist = []
#     fulldata = sp.current_user_top_tracks(time_range='medium_term')
#     # pprint(fulldata)
#     for i in range (20):  # using list1 doesn't work
#
#         # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
#         entry = fulldata['items'][i]['artists'][0]['name']   + " - " + fulldata['items'][i]['name']
#         #   + " - " + fulldata[i]['track']['album']['name']
#         fancylist.append(entry)
#     pprint(fancylist)
#     print("=============================================")
#     fancylist = []
#     fulldata = sp.current_user_top_tracks(time_range='long_term')
#     # pprint(fulldata)
#     for i in range (20):  # using list1 doesn't work
#
#         # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
#         entry = fulldata['items'][i]['artists'][0]['name']   + " - " + fulldata['items'][i]['name']
#         #   + " - " + fulldata[i]['track']['album']['name']
#         fancylist.append(entry)
#     pprint(fancylist)
#     print("=============================================    ")

# def current_func():
# fulldata = sp.audio_features("spotify:track:5VctLR5RDyzjkaFiNrxZNd")
#     pprint(fulldata)

# fancylist = []
# fulldata = sp.artist_top_tracks("spotify:artist:5fENlrINIVP0gJOtKxvORt")
# pprint(fulldata)
#
# print(type(fulldata))
# print(fulldata['tracks'][0]['name'])
# dic = {}
# spotify:track:5VctLR5RDyzjkaFiNrxZNd
# for i in range (10):
#     # dic = item
#     entry = fulldata['tracks'][i]['name']
#     fancylist.append(entry)
# pprint(fancylist)

def synergize():
    # yes I'm aware this is a pretty inefficient way of doing things and that ideally it doesn't need to get each playlist twice.
    # however it works well enough, and I'm putting effort into improving Gridline instead.
    testlist = "spotify:playlist:5NKYetvb0UeaSDcnjs7SB7"
    # use_purgelist()

    # todo --- to figure these out just see where add_tracks is going

    idlist = get_diff(utils.ROADKILL, "roadkill", utils.ROADKILL_REPO, "roadkill repo", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.ROADKILL_REPO)  # add tracks from roadkill to rkrepo
        idlist.clear()

    idlist = get_diff(utils.ROADKILL_REPO, "roadkill repo", utils.ROADKILL, "roadkill", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.ROADKILL)  # add tracks from rkrepo to roadkill
        idlist.clear()

    idlist = get_diff(utils.ROADKILL_REPO, "roadkill repo", utils.ROADKILL_ARCHIVE, "roadkill archive", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.ROADKILL_ARCHIVE)
        idlist.clear()

    idlist = get_diff(utils.ROADKILL_REPO, "roadkill repo", utils.OMNI, "omniscience", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.OMNI)
        idlist.clear()

    idlist = get_diff(utils.OMNI, "omniscience", utils.OMNI_REPO, "omniscience repo", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.OMNI_REPO)
        idlist.clear()

    idlist = get_diff(utils.OMNI_REPO, "omniscience repo", utils.OMNI_ARCHIVE, "omniscience archive", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.OMNI_ARCHIVE)
        idlist.clear()
# idlist = get_diff(utils.ROADKILL, "Roadkill", utils.OMNI, "Omniscience", PlaylistGetTypes.IDS_ONLY)
#
# idlist = get_diff(utils.ROADKILL, "Roadkill", utils.OMNI, "Omniscience", PlaylistGetTypes.IDS_ONLY)

# add_tracks(idlist, testlist)
