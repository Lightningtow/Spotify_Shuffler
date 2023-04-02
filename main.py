# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import itertools
def newPlaylist(sp, old_playlist):
    from urllib.request import urlopen
    import base64
    print("getting source details")
    # destr = ""
    details = [sp.playlist(old_playlist, fields='description,name')]
    # result = sp.playlist(old_playlist, fields="description")
    # pprint(result)
    # print(desc)
    desc = ""
    name = ""
    for item in details:
        # print(item)
        name = item['name']
        # if item['description'] == "":
        # desc = "-"
        # else:
        desc = item['description']

    # print("description is: " + desc)
    desc = desc.replace('&#x27;', '\'').replace('&quot;', '"')  # un-butcher quotes
    # print("description is: " + desc)
    name = name + " (shuffled)"
    # print("desc: " + desc)

    user_id = sp.me()['id']
    print("creating new playlist")
    destination_playlist = sp.user_playlist_create(user_id, name=name, description=desc)['uri']
    cover = []
    print("getting source cover image")
    cover.extend(sp.playlist_cover_image(old_playlist))
    # print(cover['url'])
    coverurl = " "
    for item in cover:
        # print(item['url'])
        coverurl = item['url']  # get url. Dunno why it has to be a `for` loop to use [''] notation
        # print(coverurl)  # sends you 3 urls of spotify-generated art, different sizes, biggest to smallest.
        break  # Break to get only biggest

    coverstr = base64.b64encode(urlopen(coverurl).read())  # convert url to 64 bit str
    print("uploading cover image")
    sp.playlist_upload_cover_image(destination_playlist, coverstr)


def getTracks(sp, playlist_id):
    # pass a playlist id
    # returns a list of track objects

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
    print("found " + str(length) + " tracks ")

    return alltracks

def addTracks(sp, ids, destination):
    import math
    size = len(ids)

    hundreds = math.ceil(size / 100) - 1  # number of times to add 100 songs
    if size > 100:
        leftovers = size - (hundreds * 100)
    else:
        leftovers = size
    # print("hundreds " + str(hundreds))
    # print("leftovers = " + str(leftovers))
    # print(" ")
    newlist = []
    # sp.playlist_replace_items(destination_playlist, newlist)
    # print("clearing destination playlist")
    print("adding " + str(size) + " tracks")
    if size > 100:

        # pprint(songid)

        for i in range(hundreds):
            newlist = ids[i * 100:(i + 1) * 100]
            print("adding tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
            # newlist = ids[i * 50:(i + 1) * 50]
            # namelist = names[i * 50:(i + 1) * 50]
            # print("adding tracks " + str((i * 50)+1) + " - " + str((i + 1)*50))
            # pprint(namelist)
            # print(str(i+1) + ": " + songid[i])
            # track = [songid[i]]
            # print(track)
            # if left > 100:
            # sp.playlist_replace_items(destination_playlist, newlist)
            sp.playlist_add_items(destination, newlist, position=None)

            # print("successfully added tracks " + str((i * 100)+1) + " - " + str((i + 1)*100))

    print("adding tracks " + str((hundreds * 100) + 1) + " - " + str((hundreds * 100) + leftovers))
    newlist = ids[-leftovers:]  # make list of leftover songs
    # pprint(newlist)
    # sp.playlist_replace_items(destination_playlist, newlist)
    sp.playlist_add_items(destination, newlist, position=None)

def clear():
    print("it is all clear now")


def shuffle():

    import random
    import argparse
    import logging
    import spotipy
    import math
    from spotipy.oauth2 import SpotifyOAuth
    from pprint import pprint

    # $env:"credentials" SPOTIPY_CLIENT_ID='afcaf22da9c746aca1fac02d7bb75712'
    # $env:"credentials" SPOTIPY_CLIENT_SECRET='9c632b6d09ca4f0582853f425a006b41'
    # $env:"credentials" SPOTIPY_REDIRECT_URI='http://localhost'
    logger = logging.getLogger('examples.add_tracks_to_playlist')
    # logging.basicConfig(level='DEBUG')
    scope = 'playlist-modify-public'

    scopes = "user-library-read playlist-modify-private " \
             "playlist-modify-public app-remote-control streaming ugc-image-upload"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="afcaf22da9c746aca1fac02d7bb75712",
                                                   client_secret="9c632b6d09ca4f0582853f425a006b41",
                                                   redirect_uri="http://localhost",
                                                   scope=scopes))

    old_playlist = "init"
    # old_playlist = 'spotify:playlist:0yf6lcDHKrYIiSBWlGdHxY'  # green day jr
    old_playlist = "spotify:playlist:5ts96D5tgtlxwXSWKwGvsm"  # roadkill
    # old_playlist = "spotify:playlist:3PXFZxy8QdBmvFHCYyErw3"  # omniscience
    destination_playlist = "spotify:playlist:5LfLerilfRupBAyjiIhrYN"  # test playlist

    print("copy from which playlist?")
    print("<1> green day jr")
    print("<2> roadkill")
    print("<3> omniscience")
    print("<4> test_11")
    print("<5> grandson + k.flay")

    choice = input("> ")
    if choice == '1':
        old_playlist = 'spotify:playlist:0yf6lcDHKrYIiSBWlGdHxY'  # green day jr
    elif choice == '2':
        old_playlist = "spotify:playlist:5ts96D5tgtlxwXSWKwGvsm"  # roadkill
    elif choice == '3':
        old_playlist = "spotify:playlist:3PXFZxy8QdBmvFHCYyErw3"  # omniscience
    elif choice == '4':
        old_playlist = "spotify:playlist:1KJW3gIz3EGTviDLDwb7xa"  # test_11
    elif choice == '5':
        old_playlist = "spotify:playlist:0jFqFVRXUsOL6xjJOeaLIM"  # grandson + k.flay
    else:
        print("invalid, you loser")
        exit(-1)



    newPlaylist(sp, old_playlist)

    # print(destination_playlist)
    # print("uploading name")
    # sp.playlist_change_details(destination_playlist, name=name)
    # print("uploading description")
    # sp.playlist_change_details(destination_playlist, description=desc)

    # if desc != "":
    #     print("uploading description")
    #     sp.playlist_change_details(destination_playlist, description=desc)
    # else:
    #     print("    no description")

    ids = []
    # names = []
    # remove all local songs
    i = 0  # just for counting how many tracks are local
    alltracks = getTracks(sp, old_playlist)


    # print(type(alltracks))
    for item in alltracks:

        # print(item['track']['name'])

        if item['is_local']:  # or item['track']['resume_point'] is not None
            # alltracks.remove(item)  # apparently this just removes the next one
            i += 1
            print("    removing local track")
            # continue
        elif item['track']['type'] == 'episode':  # or item['track']['resume_point'] is not None
            # alltracks.remove(item)  # same here
            i += 1
            print("    removing podcast")
            # continue

        elif item['track']['id'] is not None:  # and item['track']['description'] is None
            # print(item['track']['id'])
            # print("ADDING " + item['track']['name'])
            # names.append(item['track']['name'])
            ids.append(item['track']['id'])
            # ids.extend(item)

    # pprint(ids)
    # pprint(names)
    # if len(ids) != len(names):
    #     print("IDS AND NAMES DESYNCHRONIZED")
    #     exit(666)
    # print("adding " + str(len(ids)) + " tracks to new playlist")
    # print(type(ids))
    # print(len(ids))
    # print(len(names))
    # pprint(names)
    print("shuffling tracks")
    random.shuffle(ids)
    # names = "deleted"  # since it's desynchronized from ids
    addTracks(sp, ids, destination_playlist)

def main():
    shuffle()
    # print("<1> shuffle")
    # print("<2> clear")
    # choice = input("> ")
    # if choice == 1:
    #     shuffle()
    # elif choice == 2:
    #     clear()
    # else:
    #     print("invalid, you loser")


if __name__ == '__main__':
    main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
