

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

def get_queue():
    sp = auth()
    queuelist = sp.queue()
    # for item in queuelist:
        # item['track']['uri']
    pprint(queuelist)
    print(len(queuelist['queue']))

def get_diff(uri_1, name1, uri_2, name2, return_type):
    # take list1, and for each song, if it's in list2, remove it from the list.
    # so you end up with a list of all songs from list1 that aren't in list2
    # list1 is roadkill and list2 is omniscience, for example

    print("comparing", name1, "with", name2)
    # returns fulldata cause fuck it, better to have it and parse it later, than need it and not have it

    print("getting items from", name1)
    list1 = get_tracks(playlist_id=uri_1, return_type=PlaylistGetTypes.FULLDATA, return_local=False)
    # pprint(list1[0]['track']['album']['name'])
    # print(list1[0]['track']['name']  + " - " + list1[0]['track']['artists'][0]['name'])

    # exit(42)
    print("getting items from", name2)
    list2 = get_tracks(playlist_id=uri_2, return_type=PlaylistGetTypes.FULLDATA, return_local=False)

    newlist = []
    # print('\n', len(list1))
    # print('\n', len(list2))

    inboth = False
    for item in list1:
        inboth = False
        for item2 in list2:
            # print
            if item['track']['uri'] == item2['track']['uri']:  # todo why did this crash
                # print("removing", item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
        # if item['track']['uri'] in list2:
                inboth = True
                break
                # try:
                #     list1.remove(item)
                # except ValueError:
                #     pass
        if not inboth:
            newlist.append(item)
                # break  # continue to next item in list1
        # else:

    # list1.sort()
    fancylist = []
    datalist = []
    for item in newlist:  # using list1 doesn't work
        if return_type == PlaylistGetTypes.FULLDATA:
            datalist.append(item)
        elif return_type == PlaylistGetTypes.IDS_ONLY:
            datalist.append(item['track']['uri'])
        # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
        entry = item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name']
        fancylist.append(entry)
        # print(item['name'])

    fancylist.sort()
    print("found", len(fancylist), "songs in", name1, "that weren't in", name2)
    if fancylist != []:
        print(" ")
        pprint(fancylist)
        print(" ")
    # print('\n', len(fancylist))

    return datalist

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
                print("found dupe: " + item['name'])   #  todo THIS DOESNT WORK PROPERLY
                                                        #  'fierce' MACTHES WITH 'Fierce Femmes'
                dupes += 1  # don't bother with renaming them

                item['name'] = item['name'] + " [" + str(dupes) + "]"

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

def get_tracks(playlist_id, return_type, return_local):

    # pass a playlist id
    # return_type is from enum above. Whether to return only a list of ids, or a giant list of all data
    # if return_local is false, returns a list of URI objects
    # if return_local is true, returns a 2-elem list of: [URI objects <list>, amount of local tracks <int>]
    # THIS WILL NEVER RETURN A LOCAL TRACK ID
    # URI objects are like `spotify:track:1wtTpKbhYqojzFaLEJMHbZ` or `spotify:episode:1oq6xOHkCYXMlplvcN4nnn`
    # playlist ID is assumed to be valid

    # if return_type == IDS_ONLY:
    # todo-- returns a 2-elem list of: [URI objects <list>, amount of local tracks <int>]
    # ^ this is intentional, just highlighted
    sp = auth()

    alltracks = []
    print("\tgetting items 1 - 100")

    result = sp.playlist_items(playlist_id, additional_types=['track'])
    # print(result)
    alltracks.extend(result['items'])
    # if playlist is larger than 100 songs, continue loading it until end
    i = 0
    while result['next']:
        i += 1
        print("\tgetting items " + str((i * 100) + 1) + " - " + str((i + 1) * 100))  # todo-- this is the 'getting items' line
        result = sp.next(result)
        alltracks.extend(result['items'])

    length = len(alltracks)
    print("\tfound " + str(length) + " items")

    # pprint(alltracks)

    if return_type == PlaylistGetTypes.FULLDATA:  # THE BELOW PORTION SCRUBS OUT NON-ID DATA
        if not return_local:                # todo uhh does it tho
            for item in alltracks:  # scrub alltracks and convert to list of just ids
                if item['is_local']:
                    alltracks.remove(item)
                    # removed_tracks += 1
        return alltracks
    # todo-- everything beyond this is IDS ONLY
    # ^ intentional

    local_tracks = 0  # for both keeping and removing locals
    ids = []
    for item in alltracks:  # scrub alltracks and convert to list of just ids
        # print(item['track']['name'])

        if item['is_local']:  # if its a local track
            local_tracks += 1
            print("    removing local track")  # lol doesn't actually remove from alltracks, just doesn't add to ids
            # elif return_local:
            #     pass
            #     ids.append(item['track']['uri'])
            # else:
            #     print("error: invalid value passed for keep_local in get_tracks(), please report this")
        # elif item['track']['type'] == 'episode':
        #     print("    removing podcast")

        elif item['track']['id'] is not None:
            # ids.append(item['track']['id'])

            ids.append(item['track']['uri'])
    # print(playlist_id)

    if return_type == PlaylistGetTypes.IDS_ONLY:
        if return_local:
            # tup : tuple[int | list, ...]= (removed_locals, ids)
            # ids.append(ids[0])
            # ids[0] = removed_locals
            return [ids, local_tracks]
        else: # if not adding local tracks
            # if local_tracks > 0:
            #     print(local_tracks, "local tracks removed. See README for details")
            return [ids, local_tracks]
    else:
        print("error, please report. Reason: invalid return_type enum arg passed to get_tracks()")
        exit(-1)

