# from data import AUTH

# def get_name_from_playlist_uri(uri):
#     sp = AUTH
#     fulldata = sp.playlist(uri, fields='name, uri')  # gotta refer to the string element, not the list itself. `Thus uri[0]`
#     print(fulldata['name'])
# return fulldata['name']
import secrets
import sys
from pprint import pprint

import spotipy
from spotipy import SpotifyOAuth

from data import SCOPES


def ask_int(query, low, high):
    while True:
        choice = input(query + "\n\n> ")
        try:
            choice = int(choice)
            if choice > high or choice < low:
                print("Please enter an integer between " + str(low) + " and " + str(high))
                continue
            return choice
        except ValueError:
            print("Please enter an integer between " + str(low) + " and " + str(high))


def auth():
    print("authing")
    sp = ""
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='invalid',
                                                       client_secret='invalid',
                                                       redirect_uri='http://localhost:8080',
                                                       scope=SCOPES))
    except Exception:
        print("caught on sp = spotipy")
    print("after auth request")
    try:
        sp.me()
    except Exception:
        print("caught on sp.me()")
    print("end authing")
    # from dotenv import load_dotenv
    import dotenv

    import os

    dotenv.load_dotenv()

    # print(os.environ.get('SPOTIPY_CLIENT_ID'))
    # print(os.environ.get('SPOTIPY_CLIENT_SECRET'))
    # print(os.environ.get('http://localhost:8080'))


    # dotenv.load_dotenv(f)
    #
    # print(os.environ["SPOTIPY_CLIENT_ID"])  # outputs "value"
    # os.environ["SPOTIPY_CLIENT_ID"] = "aaaa"
    # print(os.environ['SPOTIPY_CLIENT_ID'])  # outputs 'newvalue'
    #
    # # Write changes to .env file.
    # dotenv.set_key(f, "SPOTIPY_CLIENT_ID", os.environ["SPOTIPY_CLIENT_ID"])

    # print(os.environ.get('SPOTIPY_CLIENT_ID'))

    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='',
                                                       client_secret='',
                                                       redirect_uri='http://localhost:8080',
                                                       scope=SCOPES))
        # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES))

        # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, open_browser=False))
        # if there's a valid .cache, just works regardless of .env validity
        # if nothing provided, automatically tries to pull from env
        # if env invalid, fails
        # the open_browser=false prevents from getting stuck if the user inputs invalid client
        # there's just no way to consistently have it automatically open in a browser tab
        #      and still have it behave properly if the user provides invalid shit
        # and it still provides the standard "allow app to access your data?" prompt
        sp.me()
        # pprint(sp.me())
    except spotipy.oauth2.SpotifyOauthError:
        print("invalid credentials")
        print("\ncreating new authentication cache")
        file = open(".env", 'w')  # creates a new file if none exists. Else overwites existing file
        file.close()
        credlist = ["", "", ""]
        print("see the README file for more details")
        credlist[0] = input("\nplease enter your client ID\n> ") + '\n'
        credlist[1] = input("please enter your client secret\n> ") + '\n'
        # credlist[2] = input("please confirm your callback URI \nthis should be `http://localhost:8080`\n> ")
        credlist[2] = input("please enter your callback URI\n> ") + '\n'

        # cid = input("\nplease enter your client ID\n> ") + '\n'
        # secret = input("please enter your client secret\n> ") + '\n'
        # callback = input("please confirm your callback URI \nthis should be `http://localhost:8080`\n> ") + '\n'
        # credlist[2] = 'http://localhost:8080'
        credlist = [x.strip("'").strip('\n') for x in credlist]
        # cid = cid.strip("'").strip('\n')
        # secret = secret.strip("'").strip('\n')
        # callback = callback.strip("'").strip('\n')

        print("updating credentials cache")
        f = dotenv.find_dotenv()

        # print(cid + " " + secret + " " + callback)

        # print("\tbefore")
        # print(os.environ.get('SPOTIPY_CLIENT_ID'))
        # print(os.environ.get('SPOTIPY_CLIENT_SECRET'))
        # print(os.environ.get('SPOTIPY_REDIRECT_URI'))
        os.environ["SPOTIPY_CLIENT_ID"] = credlist[0]
        os.environ["SPOTIPY_CLIENT_SECRET"] = credlist[1]
        os.environ["SPOTIPY_REDIRECT_URI"] = credlist[2]
        # os.environ["SPOTIPY_CLIENT_ID"] = cid
        # os.environ["SPOTIPY_CLIENT_SECRET"] = secret
        # os.environ["SPOTIPY_REDIRECT_URI"] = callback
        # print("\tmid")
        # print(os.environ.get('SPOTIPY_CLIENT_ID'))
        # print(os.environ.get('SPOTIPY_CLIENT_SECRET'))
        # print(os.environ.get('SPOTIPY_REDIRECT_URI'))
        dotenv.set_key(f, "SPOTIPY_CLIENT_ID", os.environ["SPOTIPY_CLIENT_ID"])
        dotenv.set_key(f, "SPOTIPY_CLIENT_SECRET", os.environ["SPOTIPY_CLIENT_SECRET"])
        dotenv.set_key(f, "SPOTIPY_REDIRECT_URI", os.environ["SPOTIPY_REDIRECT_URI"])
        # print("\tafter")
        # print(os.environ.get('SPOTIPY_CLIENT_ID'))
        # print(os.environ.get('SPOTIPY_CLIENT_SECRET'))
        # print(os.environ.get('SPOTIPY_REDIRECT_URI'))
        return auth()
    # return auth()

    print("end func")
    sys.exit(3)
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
    #                                                client_secret=secret,
    #                                                redirect_uri=callback,
    #                                                scope=SCOPES))
    # better to ask forgiveness than permission right?
    # first this just tries to use an existing .cache file
    # if that doesn't work, prompts user for


    # print("testing credentials. See the readme for if you get stuck here")
    # print('if your browser shows an error like "INVALID_CLIENT: Invalid client" ')
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES))
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
    #                                                client_secret=secret,
    #                                                redirect_uri=callback,
    #                                                scope=SCOPES))
    # pprint(sp)
    #
    # sp.me()
