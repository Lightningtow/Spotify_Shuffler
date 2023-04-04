import logging
import os
# from pprint import pprint
# import playlists.txt
from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth
# from data import SCOPES, FILEPATH, AUTH
from get_add_tracks import get_all_playlists_from_user
from utils import ask_int

# called by shuffle() to determine which playlist to shuffle
# and by remove_playlist
def choose_playlist(query_arg, only_editable):
    # logger = logging.getLogger('chooser')
    logging.basicConfig(level='FATAL')  # else it'll display errors for invalid entries

    # returns a playlist id from all the playlists the user has



    pdict = get_all_playlists_from_user(get_only_editable=only_editable)
        # pprint(y)
    # print(playlistdict.items())
    i = 0
    for name in pdict:
        i += 1
        print("<" + str(i) + "> " + name)  # pdict[name] to get value

    print("\n<0> cancel")

    query = "\n" + query_arg  # quary is passed as argument lol

    # pprint(pdict.values()[3])
    names = list(pdict.keys())
    ids = list(pdict.values())

    choice = ask_int(query, 0, i) - 1

    # print(str(ids[choice]) + " - " + names[choice])

    if choice == -1:
        return "CANCELLED"

    # print("returning " + ids[choice])
    return ids[choice]

#
# def old_choose_playlist(query):
#
#
#
#     sp = AUTH
#
#     try:
#         file = open(FILEPATH, 'r')
#         file.close()
#     except FileNotFoundError:
#         print("playlists.txt not found, creating new one")
#         file = open(FILEPATH, 'w')  # creates a new file if none exists. Else overwites existing file
#         file.close()
#
#     cleanup_needed = False
#     print("reading playlists...")
#     with open(FILEPATH, 'r') as file:
#         ids = file.readlines()
#
#         if not ids:  # if ids == []:
#             print("No playlists found. Please add a playlist URI to shuffle\n")
#             return "PLAYLISTS.TXT_IS_EMPTY"
#
#         # pprint(ids)
#         datadict = []
#         for item in ids:  # iterate through playlists.txt
#             try:
#                 fulldata = sp.playlist(item, fields='name, uri')  # get data about id
#                 # takes forever because `sp.playlist` is 1 playlist per request. Even though only getting the two datapoints
#
#                 if fulldata in datadict:  # if duplicate
#                     print("duplicate found")
#                     cleanup_needed = True
#                     continue
#                 # pprint(fulldata)
#                 datadict.append(fulldata)
#             except spotipy.exceptions.SpotifyException:
#                 cleanup_needed = True
#                 print('invalid playlist URI: "' + item.replace("\n", "") + '" ')  # replace to remove linebreak
#
#         file.close()
#
#     if cleanup_needed:  # if dupes or invalid uris in playlists.txt
#         print("removing duplicates and invalid URIs")
#         with open(FILEPATH, 'w') as file:
#             added = []
#             first = True
#             for item in datadict:  # iterate through dictionary
#                 if first:
#                     file.write(item['uri'])
#                     added.append(item)
#                 else:
#                     if item not in added:  # skip duplicates
#                         file.write('\n' + item['uri'])
#                 first = False
#             file.close()
#
#     i = 0
#     query += "\n"  # quary is passed as argument lol
#     for item in datadict:  # list all playlists
#         i += 1
#         # print("<" + str(i) + "> " + item['name'])
#         query += ("\n<" + str(i) + "> " + item['name'] + '')
#
#     query += "\n\n<0> cancel"
#
#     choice = ask_int(query, 0, i) - 1
#
#     if choice == -1:
#         return "CANCELLED"
#
#
#     return datadict[choice]['uri']
