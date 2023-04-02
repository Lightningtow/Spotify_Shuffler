from src.add_tracks import add_tracks
from src.choose_playlist import choose_playlist
from src.get_tracks import get_tracks
from src.new_playlist import new_playlist


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


    source_playlist = choose_playlist(sp)

    # exit(42)
    destination_playlist = new_playlist(sp, source_playlist)

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
    alltracks = get_tracks(sp, source_playlist)


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


    print("shuffling tracks")
    random.shuffle(ids)
    add_tracks(sp, ids, destination_playlist)



def main():
    shuffle()



if __name__ == '__main__':
    main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
