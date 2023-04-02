def new_playlist(sp, old_playlist):
    from urllib.request import urlopen
    import base64
    print("getting source details")
    # destr = ""
    details = [sp.playlist(old_playlist, fields='description,name')]
    # result = sp.playlist(old_playlist, fields="description")
    # pprint(result)
    # print(desc)
    desc = ""
    name = ""
    for item in details:
        # print(item)
        name = item['name']
        # if item['description'] == "":
        # desc = "-"
        # else:
        desc = item['description']

    # print("description is: " + desc)
    desc = desc.replace('&#x27;', '\'').replace('&quot;', '"')  # un-butcher quotes
    # print("description is: " + desc)
    name = name + " (shuffled)"
    # print("desc: " + desc)

    user_id = sp.me()['id']
    print("creating new playlist")
    destination_playlist = sp.user_playlist_create(user_id, name=name, description=desc)['uri']
    cover = []
    print("getting source cover image")
    cover.extend(sp.playlist_cover_image(old_playlist))
    # print(cover['url'])
    coverurl = " "
    for item in cover:
        # print(item['url'])
        coverurl = item['url']  # get url. Dunno why it has to be a `for` loop to use [''] notation
        # print(coverurl)  # sends you 3 urls of spotify-generated art, different sizes, biggest to smallest.
        break  # Break to get only biggest

    coverstr = base64.b64encode(urlopen(coverurl).read())  # convert url to 64 bit str
    print("uploading cover image")
    sp.playlist_upload_cover_image(destination_playlist, coverstr)

    return destination_playlist
