from pprint import pprint

from utils import auth
from getters import get_all_playlists_from_user

def purge():
    return


# def purge_song(id):
def purge_song():
    id = "spotify:track:6LQJIsR9T0AoHcfzmXTVot"
    lists = get_all_playlists_from_user(get_only_editable=True, return_count=42)
    pprint(lists, sort_dicts=False)
