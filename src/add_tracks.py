from pprint import pprint


def add_tracks(sp, ids, destination):
    import math
    size = len(ids)
    hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    leftovers = size - (hundreds * 100)  # number of tracks to add for the last non-100 chunk


    newlist = []
    # sp.playlist_replace_items(destination_playlist, newlist)
    # print("clearing destination playlist")
    if size > 100:
        print("adding " + str(size) + " tracks")
        # pprint(songid)

        for i in range(hundreds):
            newlist = ids[i * 100:(i + 1) * 100]
            # pprint(newlist)
            print("adding tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))

            # print(str(i+1) + ": " + songid[i])
            # track = [songid[i]]
            # print(track)

            sp.playlist_add_items(destination, newlist, position=None)

            # print("successfully added tracks " + str((i * 100)+1) + " - " + str((i + 1)*100))

    print("adding tracks " + str((hundreds * 100) + 1) + " - " + str((hundreds * 100) + leftovers))
    newlist = ids[-leftovers:]  # make list of leftover songs
    # pprint(newlist)
    sp.playlist_add_items(destination, newlist, position=None)
