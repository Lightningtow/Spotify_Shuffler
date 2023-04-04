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
import socket

# from utils import set_credentials


def main():
    from utils import auth

    def is_connected():
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            print("testing connection to Spotify")
            sock = socket.create_connection(("www.spotify.com", 80))
            if sock is not None:
                # print('Closing socket')
                sock.close()
            return True
        except OSError:
            pass
        return False



    if is_connected():
        print("successfully pinged Spotify")
    else:
        print("can't connect to Spotify")
        print("please try again with an internet connection")
        print("press Return to exit")
        sys.exit(-1)


    # sp = auth()

    # infin()

    # input("continue")
    # logger = logging.getLogger('chooser')
    logging.basicConfig(level='FATAL')  # else it'll display errors for invalid entries

    # NOTE! Pasting in something with trailing newlines will bug out the ide,
    #   however on cmd it'll just remove the newlines for you and work fine.

    # input("here")

    from utils import auth  # , get_name_from_playlist_uri
    # from data import AUTH  # have to put this here, in case the user needs to provide client creds
    # print("testing user app credentials")
    # while True:
    #     sp = auth()
    #     if sp != "INVALID":
    #         break
    #     print("creating new credentials cache")
    #     set_credentials()

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
        query = "\n<1> shuffle in place\n" \
                "<2> create new shuffled playlist\n" \
                "\n<0> exit program"
        choice = ask_int(query, 0, 2)

        if choice == 1:
            shuffle_in_place()

        elif choice == 2:
            shuffle_new()

        elif choice == 0:
            sys.exit(0)

        else:  # should never run, only happens if ask_int returns invali option
            print("error occured, invalid case in main()")
            sys.exit(-1)

if __name__ == '__main__':

    main()
