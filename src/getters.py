

import math
import os
from enum import Enum
from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth
import spotipy
from spotipy import SpotifyOAuth
import os
# from data import SCOPES, PlaylistGetTypes
from utils import auth


def get_name_from_playlist_uri(uri):
    sp = auth()
    fulldata = sp.playlist(uri, fields='name, uri')  # gotta refer to the string element, not the list itself. `Thus uri[0]`
    # print(fulldata['name'])
    return fulldata['name']

def get_all_playlists_from_user(get_only_editable, return_count):
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
    dupes = 0
    stopping = False
    while True:


        response = sp.user_playlists(username, limit=50, offset=offset)
        # results = sp.current_user_playlists(limit=50, offset=offset)
        # for i, item in enumerate(response['items']):
        for x, item in enumerate(response['items']):
            # pprint(item)
            # print(str(i) + " " + item['name'])

            if get_only_editable and item['owner']['uri'] != user_uri:  # if not editable, exclude from results
                # print(item['owner']['uri'] + " " + user_uri)
                excluded_playlists += 1
                total += 1
                continue

            if str(item['name']).isspace() or item['name'] == "":  # if playlist name blank or only whitespace

                untitled += 1

            # else:

            if item['name'] in newdict:  # if duplicate
                print("found dupe: " + item['name'])   #  THIS DOESNT WORK PROPERLY
                                                        #  'fierce' MACTHES WITH 'Fierce Femmes'
                dupes += 1  # don't bother with renaming them


            newdict[item['name']] = item['uri']
            total += 1
            if return_count != "ALL":
                if total - excluded_playlists == return_count:  # return only however many
                    stopping = True
                    break
        if stopping:  # to break nested loop
            break

        # print("len " + str(len(response['items'])))
        if len(response['items']) == 0:
            break

        # pprint(response['items']['name'])

        offset = offset + len(response['items'])


    print("retrieved " + str(total) + " playlists saved to your library")
    if excluded_playlists > 0:
        print("\texcluded " + str(excluded_playlists) + " playlists that you don't own")
    if untitled > 0:
        print("\tdisplaying " + str(untitled) + " blank playlist names. This is not a bug")
    if dupes > 0:
        print("\tdisplaying " + str(dupes) + " playlists with identical names. This is not a bug")

    print(" ")

    newdict = dict(sorted(newdict.items()))  # sort alphabetically by name
    # NOTE THAT USING PPRINT WILL DISPLAY THEM ALPHABETICALLY REGARDLESS
    # THEY ARE RETURNED WITH MOST RECENT FIRST
    # unless you do pprint(ids, sort_dicts=False)
    return newdict

class PlaylistGetTypes(Enum):
    FULLDATA = 1
    IDS_ONLY = 2
# def filter_fulL_data(keep_local):

def get_tracks(playlist_id, return_type, keep_local):

    # pass a playlist id
    # return_type is from enum above. Whether to return only a list of ids, or a giant list of all data
    # if keep_local is false, returns a list of URI objects
    # if keep_local is true, returns a 2-elem list of: [URI objects <list>, amount of local tracks <int>]
    # THIS WILL NEVER RETURN A LOCAL TRACK ID
    # URI objects are like `spotify:track:1wtTpKbhYqojzFaLEJMHbZ` or `spotify:episode:1oq6xOHkCYXMlplvcN4nnn`
    # playlist ID is assumed to be valid
    # IF FULLDATA, THIS RETURNS PLAYLISTS AND LOCAL TRACKS

    sp = auth()

    alltracks = []
    print("getting items 1 - 100")
    result = sp.playlist_items(playlist_id, additional_types=['track'])
    # print(result)
    alltracks.extend(result['items'])
    # if playlist is larger than 100 songs, continue loading it until end
    i = 0
    while result['next']:
        i += 1
        print("getting items " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
        result = sp.next(result)
        alltracks.extend(result['items'])

    length = len(alltracks)
    print("found " + str(length) + " items")

    # pprint(alltracks)

    if return_type == PlaylistGetTypes.FULLDATA:  # THE BELOW PORTION SCRUBS OUT NON-ID DATA
        return alltracks
    local = 0

    ids = []
    for item in alltracks:  # scrub alltracks and convert to list of just ids
        # print(item['track']['name'])

        if item['is_local']:
            if not keep_local:
                print("    removing local track")  # lol doesn't actually remove from alltracks, just doesn't add to ids
            elif keep_local:
                local += 1
                # ids.append(item['track']['uri'])
            else:
                print("error, invalid value passed for keep_local in get_tracks(), please report this")
        # elif item['track']['type'] == 'episode':
        #     print("    removing podcast")

        elif item['track']['id'] is not None:
            # ids.append(item['track']['id'])

            ids.append(item['track']['uri'])


    if return_type == PlaylistGetTypes.IDS_ONLY:
        if keep_local:
            return [ids, local]
        else:
            return ids
    else:
        print("error, please report. Reason: invalid return_type enum arg passed to get_tracks()")
        exit(-1)

