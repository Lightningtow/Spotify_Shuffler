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
         "playlist-read-collaborative "

# "user-library-read " \
# "streaming " \
# "app-remote-control " \

# def scopetest():
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, open_browser=False))


def auth():

    # this automatically does all the fixing creds shit within it. So you can freely call auth() without worrying
    import spotipy
    from spotipy import SpotifyOAuth
    # from data import SCOPES
    import dotenv
    import os
    # from data import SCOPES
    dotenv.load_dotenv()

    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, open_browser=False))
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


        return auth()  # try it again :D
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES))
