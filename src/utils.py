# from data import AUTH


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

# SCOPES = ""
SCOPES = "playlist-modify-private " \
        "playlist-modify-public " \
        "ugc-image-upload " \
        "playlist-read-private " \
        "playlist-read-collaborative " \
        "user-library-read " \
        "streaming " \
        "app-remote-control " \
        "user-read-playback-state " \
        "user-modify-playback-state " \
        "user-read-currently-playing " \
        "user-read-playback-position " \
        "user-top-read " \
        "user-read-recently-played " \





PURGELIST =         "spotify:playlist:3gWBGiJmlvbVJaS0CSY2Vg"
AFTERPURGE =        "spotify:playlist:0jjjbxOwDsTdf1Mq8hQUuS"
OMNI =              "spotify:playlist:3PXFZxy8QdBmvFHCYyErw3"
OMNI_REPO =         "spotify:playlist:5nWJjMM7DMOZCWYAJEgNtl"
OMNI_ARCHIVE =      "spotify:playlist:7pKIuF5jnS7lgB22AZGqAL"
ROADKILL =          "spotify:playlist:6o3HI8fSJrWEeZmhkCqSeZ"
ROADKILL_REPO =     "spotify:playlist:5ts96D5tgtlxwXSWKwGvsm"
ROADKILL_ARCHIVE =  "spotify:playlist:0HBq6MvLLiQBY9hTFw0JVE"
SINGALONG =         "spotify:playlist:3WcOpgXK1N9nf27qkimhPF"
PURGELIST_ROAD =    "spotify:playlist:1MYRwRHs71GWJNk1HunSAz"
AFTERPURGE_ROAD =   "spotify:playlist:6o1Tny80Jow5ulZjesvUuy"



TEST_11 =   "spotify:playlist:1KJW3gIz3EGTviDLDwb7xa"
TESTLIST =  "spotify:playlist:5NKYetvb0UeaSDcnjs7SB7"
# "user-library-read " \
# "streaming " \
# "app-remote-control " \

# def scopetest():
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, open_browser=False))


def auth():

    # you can freely call auth() without worrying
    import spotipy
    from spotipy import SpotifyOAuth
    # from data import SCOPES
    import dotenv  # package named 'python-dotenv'
    import os
    from dotenv import load_dotenv

    # from data import SCOPES
    # dotenvy.environ
    load_dotenv()

    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, open_browser=True))

    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, open_browser=False))

        # if there's a valid .cache, just works regardless of .env validity
        # if nothing provided, automatically tries to pull from env
        # if env invalid, fails
        # the open_browser=false prevents from getting stuck if the user inputs invalid client
        # there's just no way to consistently have it automatically open in a browser tab
        #      and still have it behave properly if the user provides invalid shit
        # and besides, open_browser=false still provides the standard "allow app to access your data?" prompt
        sp.me()
        # pprint(sp.me())
    except spotipy.oauth2.SpotifyOauthError:
        print("invalid credentials")
        print("\ncreating new authentication cache")
        file = open(".env", 'w')  # creates a new file if none exists. Else overwites existing file
        file.close()
        credlist = ["", "", ""]
        print("see the README file for more details")
        # credlist[0] = input("\nplease enter your client ID\n> ") + '\n'
        # credlist[1] = input("please enter your client secret\n> ") + '\n'
        # # credlist[2] = input("please confirm your callback URI \nthis should be `http://localhost:8080`\n> ")
        # credlist[2] = input("please enter your callback URI\n> ") + '\n'

        valid = False

        # credlist[0] = input("\nplease enter your client ID\n> ")
        # credlist[1] = input("please enter your client secret\n> ")
        # credlist = [x.strip("'").strip('\n') for x in credlist]
        while not valid:
            credlist[0] = input("\nplease enter your client ID\n> ")
            credlist[1] = input("please enter your client secret\n> ")
            credlist = [x.strip("'").strip('\n') for x in credlist]

            if not credlist[0].isalnum() or len(credlist[0]) != 32:
                print("invalid client ID")
            elif not credlist[1].isalnum() or len(credlist[1]) != 32:
                print("invalid client secret")
            else:
                valid = True

        # credlist[2] = input("please confirm your callback URI \nthis should be `http://localhost:8080`\n> ")
        credlist[2] = input("please enter your callback URI\n> ")

        print("updating credentials cache")
        f = dotenv.find_dotenv()
        os.environ["SPOTIPY_CLIENT_ID"] = credlist[0]
        os.environ["SPOTIPY_CLIENT_SECRET"] = credlist[1]
        os.environ["SPOTIPY_REDIRECT_URI"] = credlist[2]
        dotenv.set_key(f, "SPOTIPY_CLIENT_ID", os.environ["SPOTIPY_CLIENT_ID"])
        dotenv.set_key(f, "SPOTIPY_CLIENT_SECRET", os.environ["SPOTIPY_CLIENT_SECRET"])
        dotenv.set_key(f, "SPOTIPY_REDIRECT_URI", os.environ["SPOTIPY_REDIRECT_URI"])


        return auth()  # run it again with your brand new credentials
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES))
