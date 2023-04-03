



def main():
    from src.add_remove_playlist import remove_playlist


    from data import ask_int

    import sys

    from shuffle import shuffle
    from add_remove_playlist import add_playlist



    # NOTE! Pasting in something with trailing newlines will bug out the ide,
    #   however on cmd it'll just remove the newlines for you and work fine.

    while True:
        # ind = input("aof ").replace('\n','')
        # print(ind)

        choice = "a"
        query = "<1> add playlists\n" \
                "<2> remove playlists\n" \
                "<3> shuffle playlists\n" \
                "\n<0> exit program"

        choice = ask_int(query, 0, 3)
        # choice = 1
        if choice == 1:  # matchcase is neater but upgrading to 3.10 made a mess of things
            add_playlist()

        elif choice == 2:
            remove_playlist()

        elif choice == 3:
            shuffle()

        elif choice == 0:
            # x = input("press return key to exit ")
            sys.exit(0)


        else:  # should never run, only happens if ask_int returns invali option
            print("error occured, invalid case in main()")
            sys.exit(-1)






if __name__ == '__main__':
    main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
