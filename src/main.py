from __future__ import print_function

import logging
import threading

from urllib3.connectionpool import xrange

# from data import AUTH

import sys
# from shuffle import shuffle_in_place, shuffle_new
import sys
# from timeout import infin
import threading
from time import sleep
from purge import purge_song, use_purgelist
from src import utils
from src.choose_playlist import choose_playlist
from src.getters import get_name_from_playlist_uri
from src.synergize import synergize, current_func, remove_dupes


# def main():
# print("uh")

# MyApp.run(self=MyApp)

def main():

    def is_connected():
        import socket
        try:
            # connect to the host -- tells us if the host is actually reachable
            print("testing connection to Spotify")
            sock = socket.create_connection(("www.spotify.com", 80))

            if sock is not None:
                # print('Closing socket')
                sock.close()
            return True
        except OSError:
            pass
        return False

    from utils import auth
    logger = logging.getLogger('main')
    logging.basicConfig(level='FATAL')  # else it'll display errors for invalid entries


    # MyApp().run()

    if is_connected():
        print("successfully pinged Spotify")
    else:
        print("can't connect to Spotify")
        print("please try again with an internet connection")
        input("press Return to exit")
        sys.exit(-1)

    # NOTE! Pasting in something with trailing newlines will bug out the ide,
    #   however on cmd it'll just remove the newlines for you and work fine.

    # input("here")

    from utils import auth  # , get_name_from_playlist_uri


    print("authenticating...")  # can't put this in auth(), or it'd be printed all over the place
    # print("see README if you get stuck here")
    sp = auth()
    # input("aaaaaa")
    # print("authorizing in browser...")  # todo some tests here!!!!!
    print("")
    from shuffle import shuffle_in_place, shuffle_new
    from utils import ask_int
    user = sp.me()



# exit(42)
    # # try:
    # try:
    #     sp = AUTH
    #     user = sp.me()
    # except Exception as e:
    #     logging.error(traceback.format_exc())
    #     print("error authenticating, please check your internet connection")
    #
    #     uh = input("1")
    #     exit(-1)
    #
    # uh = input('2')
    # exit(-2)
    # print(user)
    print("successfully logged in as " + user['display_name'])

    while True:
        query = "\n" \
                "<1> synergize \n" \
                "<2> purge \n" \
                "<3> shuffle roadkill and omniscience \n\n" \
                "<4> shuffle in place\n" \
                "<5> create new shuffled playlist\n" \
                "<6> current test func \n" \
 \
        "\n<0> exit program"
        # "<5> purge current song\n" \

        choice = ask_int(query, 0, 6)
        if choice == 1:
            synergize()

        elif choice == 2:
            use_purgelist()

        elif choice == 3:
            print("shuffling roadkill")
            shuffle_in_place(utils.ROADKILL)

            print("\nshuffling omniscience")
            shuffle_in_place(utils.OMNI)

        elif choice == 4:
            playlist = choose_playlist("select playlist to shuffle:", only_editable=True)  # prompt user for source playlist
            if playlist == "CANCELLED":
                print("\ncancelled selection")
                continue
            else:
                shuffle_in_place(playlist)

        elif choice == 5:
            playlist = choose_playlist("select playlist to copy:", only_editable=False)  # prompt user for source playlist
            if playlist == "CANCELLED":
                print("\ncancelled selection")
                continue
            else:
                shuffle_new(playlist)

        elif choice == 6:
            remove_dupes(utils.TESTLIST)
            # current_func()

        elif choice == 0:
            sys.exit(0)

        else:  # should never run, only happens if ask_int returns invali option
            print("error occured, invalid case in main()")
            sys.exit(-1)

if __name__ == '__main__':
    # MyApp().run()
    main()
