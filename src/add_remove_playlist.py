import os
from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth

from choose_playlist import choose_playlist
from data import SCOPES, FILEPATH, AUTH


def add_playlist():
    sp = AUTH
    print("enter URI of playlist to add")
    print('URIs for playlists are formatted like this: "spotify:playlist:37i9dQZF1DX5kjCvsC5isB"')
    print("see https://community.spotify.com/t5/Spotify-for-Developers/Get-Playlist-URI-with-updated-Desktop-Look/m-p/5186546#M2364")
    uri = [input("\n> ").replace('\n', '')]  # newlines in a copy-pasted entry cause bugs

    try:
        fulldata = sp.playlist(uri[0], fields='name, uri')  # gotta refer to the string element, not the list itself. `Thus uri[0]`

        with open('../backups/playlists.txt', 'a') as file:
            file.write("\n" + fulldata['uri'])
            print('Adding playlist "' + fulldata['name'] + '" to playlists.txt')
            file.close()

    except spotipy.exceptions.SpotifyException:  # if invalid playlist uri
        print('invalid playlist uri: "' + uri[0].replace("\n", "") + '" ')  # `replace` to remove linebreak

def remove_playlist():
    # just removes the matching string from playlists.txt
    # does no other validation
    sp = AUTH

    target = choose_playlist("select playlist to remove:")

    with open(FILEPATH, 'r') as file:
        ids = file.readlines()

        if not ids:  # if ids == []:
            print("No playlists found. Please add a playlist URI\n")
            return "PLAYLISTS.TXT_IS_EMPTY"

        # pprint(ids)
        kept_ids = []  # iterate through playlists.txt
        for item in ids:
            item = item.replace("\n", "")
            if item == target:  # found target to remove
                print("removed successfully")
                continue
            kept_ids.append(item)

        file.close()
    with open(FILEPATH, 'w') as file:
        for item in kept_ids:
            file.write(item + "\n")
