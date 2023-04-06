import math
from pprint import pprint

from utils import auth


def wipe_tracks_by_id(playlist_id, tracks_to_wipe):
    # ids are the tracks to wipe
    sp = auth()

    ids = tracks_to_wipe
    size = len(ids)
    hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    leftovers = size - (hundreds * 100)  # number of tracks to add for the last non-100 chunk

    sp = auth()


    newlist = []


    if size > 100:
        print("removing " + str(size) + " items")

        for i in range(hundreds):
            newlist = ids[i * 100:(i + 1) * 100]  # make list of tracks to remove this cycle

            print("removing items " + str((i * 100) + 1) + " - " + str((i + 1) * 100))

            sp.playlist_remove_all_occurrences_of_items(playlist_id, newlist)

            # print("successfully added tracks " + str((i * 100)+1) + " - " + str((i + 1)*100))


    print("removing items " + str((hundreds * 100) + 1) + " - " + str((hundreds * 100) + leftovers))
    newlist = ids[-leftovers:]  # make list of leftover songs
    sp.playlist_remove_all_occurrences_of_items(playlist_id, newlist)

    print("done removing")
    # pprint(sp.playlist_items(playlist_id))


def add_tracks(ids, destination):
    # pass a list of track/playlist uris
    #   either like `spotify:track:1wtTpKbhYqojzFaLEJMHbZ` or `spotify:episode:1oq6xOHkCYXMlplvcN4nnn`
    # destination is a playlist uri
    # ALL ARGUMENTS ARE ASSUMED TO BE VALID
    # no return values
    # does not wipe the playlist, simply appends the tracks
    size = len(ids)
    hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    leftovers = size - (hundreds * 100)  # number of tracks to add for the last non-100 chunk

    sp = auth()


    newlist = []


    if size > 100:
        print("adding " + str(size) + " items")

        for i in range(hundreds):
            newlist = ids[i * 100:(i + 1) * 100]  # make list of tracks to add this cycle

            print("adding items " + str((i * 100) + 1) + " - " + str((i + 1) * 100))

            sp.playlist_add_items(destination, newlist, position=None)

            # print("successfully added tracks " + str((i * 100)+1) + " - " + str((i + 1)*100))


    print("adding items " + str((hundreds * 100) + 1) + " - " + str((hundreds * 100) + leftovers))
    newlist = ids[-leftovers:]  # make list of leftover songs
    sp.playlist_add_items(destination, newlist, position=None)
