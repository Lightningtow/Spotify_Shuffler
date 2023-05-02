from pprint import pprint

from src import utils
from src.edit_playlists import add_tracks, wipe_tracks_by_id
from utils import auth
from getters import get_all_playlists_from_user, get_tracks, PlaylistGetTypes


def use_purgelist():
    sp = utils.auth()

    print("getting purgelist")
    # def get_tracks(playlist_id, return_type, keep_local):
    fulldata = get_tracks(playlist_id=utils.PURGELIST, return_type=PlaylistGetTypes.FULLDATA, return_local=False)
    # get full data from purgelist

    purgenames = []
    purgelist = []  # list of only ids
    for item in fulldata:
        purgelist.append(item['track']['uri'])
        entry = item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name']
        purgenames.append(entry)

    purge_len = len(purgelist)
    if purge_len != 0:
    # target = "spotify:playlist:5LfLerilfRupBAyjiIhrYN"  # test_playlist
        print("purging", purge_len, "songs:")
        pprint(purgenames)

        print("purging Omniscience")
        sp.playlist_remove_all_occurrences_of_items(utils.OMNI, purgelist)

        print("purging Omniscience Repo")
        sp.playlist_remove_all_occurrences_of_items(utils.OMNI_REPO, purgelist)

        print("purging Roadkill")
        sp.playlist_remove_all_occurrences_of_items(utils.ROADKILL, purgelist)

        print("purging Roadkill Repo")
        sp.playlist_remove_all_occurrences_of_items(utils.ROADKILL_REPO, purgelist)

        print("adding to afterpurge")
        add_tracks(ids=purgelist, destination=utils.AFTERPURGE)  # add to afterpurge
        # pprint(purgelist)
        print("clearing purgelist")
        wipe_tracks_by_id(tracks_to_wipe=purgelist, playlist_id=utils.PURGELIST)  # clear purgelist

    else:
        print("nothing to purge")


    fulldata = fulldata.clear()
    print("\ngetting roadkill purgelist")
    # def get_tracks(playlist_id, return_type, keep_local):
    fulldata = get_tracks(playlist_id=utils.PURGELIST_ROAD, return_type=PlaylistGetTypes.FULLDATA, return_local=False)
    # get full data from purgelist

    purgenames = []
    purgelist = []  # list of only ids
    for item in fulldata:
        purgelist.append(item['track']['uri'])
        entry = item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name']
        purgenames.append(entry)

    roadpurge_len = len(purgelist)
    if roadpurge_len != 0:
        # target = "spotify:playlist:5LfLerilfRupBAyjiIhrYN"  # test_playlist
        print("purging", roadpurge_len, "songs:")
        pprint(purgenames)

        print("purging Roadkill")
        sp.playlist_remove_all_occurrences_of_items(utils.ROADKILL, purgelist)

        print("purging Roadkill Repo")
        sp.playlist_remove_all_occurrences_of_items(utils.ROADKILL_REPO, purgelist)

        print("adding to afterpurge road edition")
        add_tracks(ids=purgelist, destination=utils.AFTERPURGE_ROAD)  # add to afterpurge
        # pprint(purgelist)
        print("clearing purgelist")
        wipe_tracks_by_id(tracks_to_wipe=purgelist, playlist_id=utils.PURGELIST_ROAD)  # clear purgelist

    else:
        print("nothing to purge")
    return


# def purge_song(id):
def purge_song(id):
    id = "spotify:track:6LQJIsR9T0AoHcfzmXTVot"
    # lists = get_all_playlists_from_user(get_only_editable=True, return_count=42)
    # pprint(lists, sort_dicts=False)
