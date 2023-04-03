import logging
import os
# from pprint import pprint
# import playlists.txt
from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth
from data import SCOPES, ask_int, FILEPATH, AUTH



def choose_playlist(query):
    # called by shuffle() to determine which playlist to shuffle
    # maybe? could work for getting playlists for other reasons



    # logger = logging.getLogger('chooser')
    logging.basicConfig(level='FATAL')  # else it'll display errors for invalid entries

    sp = AUTH

    try:
        file = open(FILEPATH, 'r')
        file.close()
    except FileNotFoundError:
        print("playlists.txt not found, creating new one")
        file = open(FILEPATH, 'w')  # creates a new file if none exists. Else overwites existing file
        file.close()

    cleanup_needed = False
    print("reading playlists...")
    with open(FILEPATH, 'r') as file:
        ids = file.readlines()

        if not ids:  # if ids == []:
            print("No playlists found. Please add a playlist URI to shuffle\n")
            return "PLAYLISTS.TXT_IS_EMPTY"

        # pprint(ids)
        datadict = []  # iterate through playlists.txt
        for item in ids:
            try:  # takes forever because `sp.playlist` is 1 playlist per request. Even though only getting the two datapoints
                fulldata = sp.playlist(item, fields='name, uri')  # get data about id
                if fulldata in datadict:  # if duplicate
                    print("duplicate found")
                    cleanup_needed = True
                    continue
                # pprint(fulldata)
                datadict.append(fulldata)
            except spotipy.exceptions.SpotifyException:
                cleanup_needed = True
                print('invalid playlist URI: "' + item.replace("\n", "") + '" ')  # replace to remove linebreak

        file.close()

    if cleanup_needed:  # if dupes or invalid uris in playlists.txt
        print("removing duplicates and invalid URIs")
        with open(FILEPATH, 'w') as file:
            added = []
            first = True
            for item in datadict:  # iterate through dictionary
                if first:
                    file.write(item['uri'])
                    added.append(item)
                else:
                    if item not in added:  # skip duplicates
                        file.write('\n' + item['uri'])

                first = False
            file.close()


    # pprint(namedict)
    i = 0
    # query = "\nselect playlist to shuffle:"
    query += "\n"
    for item in datadict:  # list all playlists
        i += 1
        # print("<" + str(i) + "> " + item['name'])
        query += ("\n<" + str(i) + "> " + item['name'] + '')

    query += "\n\n<0> cancel"

    choice = ask_int(query, 0, i) - 1

    if choice == -1:
        return "CANCELLED"
    # print(namedict[choice]['name'])
    # print(namedict[choice]['uri'])

    return datadict[choice]['uri']
