from pprint import pprint
from urllib.request import urlopen
import base64

import os
import spotipy
from spotipy import SpotifyOAuth
from utils import auth


def copy_playlist_info(source_playlist):
    # create a new playlist based on the old one
    # carries over name, description, cover art if custom
    # if not custom, leaves cover art so it can be properly auto-generated
    # does not carry over tracks/playlists
    sp = auth()

    print("getting source details")
    # print(source_playlist)
    details = [sp.playlist(source_playlist, fields='description,name')]
    # pprint(details)
    # desc = ""  # playlist description
    # name = ""
    # for item in details:
    name = details[0]['name']  # playlist name
    desc = details[0]['description']  # if description is blank, doesn't matter for `sp.user_playlist_create`


    desc = desc.replace('&#x27;', '\'').replace('&quot;', '"').replace('&#x2F;', '/')  # un-butcher special chars
    name = name + " (shuffled)"  # append 'shuffled' to name of new playlist

    user_id = sp.me()['id']
    print("creating new playlist")
    destination_playlist = sp.user_playlist_create(user_id, name=name, description=desc)['uri']  # create new playlist

    print("getting source cover image")
    cover = []
    cover.extend(sp.playlist_cover_image(source_playlist))
    coverurl = " "
    i = 0
    for item in cover:  # runs either 1 or 3 times depending on type of cover image
        i += 1
        # print(item['url'])
        coverurl = item['url']  # get url.

    if i == 1:
        # spotify will send you 1 image for custom covers, or 3 for the Spotify-generated covers of 4 album arts
        # so if there's only one image, means custom image and should be copied
        # else leave it blank so it overwrites
        coverstr = base64.b64encode(urlopen(coverurl).read())  # convert url to 64 bit str
        print("uploading cover image")
        sp.playlist_upload_cover_image(destination_playlist, coverstr)
    else:
        print("    no cover image")

    return destination_playlist
