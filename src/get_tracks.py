def get_tracks(sp, playlist_id):
    # pass a playlist id
    # returns a list of track objects

    alltracks = []
    print("getting tracks 1 - 100")
    result = sp.playlist_items(playlist_id, additional_types=['track'])
    alltracks.extend(result['items'])
    # if playlist is larger than 100 songs, continue loading it until end
    i = 0
    while result['next']:
        i += 1
        print("getting tracks " + str((i * 100) + 1) + " - " + str((i + 1) * 100))
        result = sp.next(result)
        alltracks.extend(result['items'])

    length = len(alltracks)
    print("found " + str(length) + " tracks ")

    return alltracks