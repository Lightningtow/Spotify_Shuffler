

import math
import os
from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth
import spotipy
from spotipy import SpotifyOAuth
import os
from data import SCOPES, PlaylistGetTypes
from utils import auth
def get_all_playlists_from_user(get_only_editable):
    # returns a dict of all user playlists
    # key = displayname, value = id
    # sorted alphabetically by displayname
    sp = auth()


    offset = 0
    user = sp.me()
    username = user['id']
    # print(username)
    newdict = {}
    print("getting your playlists...")
    user_uri = user['uri']
    # print(user_uri)
    total = 0
    excluded_playlists = 0
    untitled = 0
    while True:

        response = sp.user_playlists(username, limit=50, offset=offset)
        # results = sp.current_user_playlists(limit=50, offset=offset)
        # for i, item in enumerate(response['items']):
        for x, item in enumerate(response['items']):
            # pprint(item)
            # print(str(i) + " " + item['name'])


            if get_only_editable and item['owner']['uri'] != user_uri:
                # print(item['owner']['uri'] + " " + user_uri)
                excluded_playlists += 1
                total += 1
                continue

            if str(item['name']).isspace() or item['name'] == "":  # if playlist name blank or only whitespace


                # item['name'] = "-[untitled playlist]"
                # newdict[u] = item['uri']
                # print(u)
                untitled += 1

            # else:

            if item['name'] in newdict:  # if duplicate
                dupes = 0
                while True:  # ensure multiple dupes get named properly
                    dupes += 1
                    # print("duplicate!")
                    # print(newdict[item['name']])
                    newname = (item['name'] + " [" + str(dupes) + "]")
                    # print(newname)
                    if newname not in newdict:
                        item['name'] = newname
                        break

            newdict[item['name']] = item['uri']
            total += 1


            # print("%d %s" % (x+1+(i*50), item['name']))


        # print("len " + str(len(response['items'])))
        if len(response['items']) == 0:
            break

        # pprint(response['items']['name'])
        offset = offset + len(response['items'])


    print("found " + str(total) + " playlists saved to your library")
    if get_only_editable:
        print("\texcluded " + str(excluded_playlists) + " playlists that you don't own")
    if untitled > 0:
        print("\tfound " + str(untitled) + " playlist names that are only whitespace. This is not a bug")
    print(" ")

    newdict = dict(sorted(newdict.items()))  # sort alphabetically by name
    return newdict

def get_tracks(playlist_id, return_type):
    # pass a playlist id
    # returns a list of track objects

    sp = AUTH

    alltracks = []
    print("getting tracks 1 - 100")
    result = sp.playlist_items(playlist_id, additional_types=['track'])
    # print(result)
    alltracks.extend(result['items'])
    # if playlist is larger than 100 songs, continue loading it until end
    i = 0
    while result['next']:
        i += 1
        print("getting tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
        result = sp.next(result)
        alltracks.extend(result['items'])

    length = len(alltracks)
    print("found " + str(length) + " tracks")

    if return_type == PlaylistGetTypes.FULLDATA:
        return alltracks


    ids = []
    for item in alltracks:  # scrub alltracks and convert to list of just ids
        # print(item['track']['name'])

        if item['is_local']:
            print("    removing local track")  # lol doesn't actually remove from alltracks, just doesn't add to ids

        elif item['track']['type'] == 'episode':
            print("    removing podcast")

        elif item['track']['id'] is not None:

            ids.append(item['track']['id'])
    if return_type == PlaylistGetTypes.IDS_ONLY:
        return ids
    else:
        print("error, please report. Reason: invalid return_type enum arg passed to get_tracks()")
        exit(-1)
#
# def old_get_tracks(playlist_id):
#     # pass a playlist id
#     # returns a list of track objects
#
#     sp = AUTH
#
#     alltracks = []
#     print("getting tracks 1 - 100")
#     result = sp.playlist_items(playlist_id, additional_types=['track'])
#     print(result)
#     alltracks.extend(result['items'])
#     # if playlist is larger than 100 songs, continue loading it until end
#     i = 0
#     while result['next']:
#         i += 1
#         print("getting tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
#         result = sp.next(result)
#         alltracks.extend(result['items'])
#
#     length = len(alltracks)
#     print("found " + str(length) + " tracks")
#
#     return alltracks

def add_tracks(ids, destination):
    # pass a list of plaintext uris in string form
    # destination is a playlist uri
    size = len(ids)
    hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    leftovers = size - (hundreds * 100)  # number of tracks to add for the last non-100 chunk

    sp = AUTH


    newlist = []


    if size > 100:
        print("adding " + str(size) + " tracks")

        for i in range(hundreds):
            newlist = ids[i * 100:(i + 1) * 100]  # make list of tracks to add this cycle

            print("adding tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))

            sp.playlist_add_items(destination, newlist, position=None)

            # print("successfully added tracks " + str((i * 100)+1) + " - " + str((i + 1)*100))


    print("adding tracks " + str((hundreds * 100) + 1) + " - " + str((hundreds * 100) + leftovers))
    newlist = ids[-leftovers:]  # make list of leftover songs
    sp.playlist_add_items(destination, newlist, position=None)

