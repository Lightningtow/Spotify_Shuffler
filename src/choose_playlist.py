from pprint import pprint
# import playlists.txt

def choose_playlist(sp):
    # import os
    #
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))

    with open('src/playlists.txt', 'r') as file:
        ids = file.readlines()
        # pprint(ids)
        namedict = []
        for item in ids:
            name = sp.playlist(item, fields='name, uri')
            # print(name)
            namedict.append(name)
        file.close()
        # pprint(namedict)
    i = 0
    print("select playlist to shuffle:")
    for item in namedict:
        i += 1
        print("<" + str(i) + "> " + item['name'])
    choice = int(input("> "))-1  # todo input validation
    # print(namedict[choice]['name'])


    return namedict[choice]['uri']