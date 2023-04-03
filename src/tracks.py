import math
import os
import spotipy
from spotipy import SpotifyOAuth
import spotipy
from spotipy import SpotifyOAuth
import os
from data import SCOPES, AUTH


def get_tracks(playlist_id):
    # pass a playlist id
    # returns a list of track objects

    sp = AUTH



    alltracks = []
    print("getting tracks 1 - 100")
    result = sp.playlist_items(playlist_id, additional_types=['track'])
    alltracks.extend(result['items'])
    # if playlist is larger than 100 songs, continue loading it until end
    i = 0
    while result['next']:
        i += 1
        print("getting tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
        result = sp.next(result)
        alltracks.extend(result['items'])

    length = len(alltracks)
    print("found " + str(length) + " tracks\n")

    return alltracks

def add_tracks(ids, destination):
    size = len(ids)
    hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    leftovers = size - (hundreds * 100)  # number of tracks to add for the last non-100 chunk


    sp = AUTH


    newlist = []
    # sp.playlist_replace_items(destination_playlist, newlist)  # used to clear playlist
    # print("clearing destination playlist")
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
