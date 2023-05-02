from pprint import pprint

from src import utils
from src.edit_playlists import add_tracks
from src.getters import get_diff, PlaylistGetTypes
from src.purge import use_purgelist
from src.utils import auth
def current_func():
    sp = auth()
    # fulldata = sp.devices()
    # pprint(fulldata)
    sp.pause_playback()

# def current_func():
#     sp = auth()
#     # fulldata = sp.current_playback()
#     # fulldata['item']['album']['available_markets'] = ""
#     # fulldata['item']['available_markets'] = ""
#
#     fancylist = []
#     fulldata = sp.current_user_top_tracks(time_range='short_term')
#     # pprint(fulldata)
#     for i in range (20):  # using list1 doesn't work
#
#     # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
#         entry = fulldata['items'][i]['artists'][0]['name']   + " - " + fulldata['items'][i]['name']
#         #   + " - " + fulldata[i]['track']['album']['name']
#         fancylist.append(entry)
#     pprint(fancylist)
#     print("=============================================")
#     fancylist = []
#     fulldata = sp.current_user_top_tracks(time_range='medium_term')
#     # pprint(fulldata)
#     for i in range (20):  # using list1 doesn't work
#
#         # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
#         entry = fulldata['items'][i]['artists'][0]['name']   + " - " + fulldata['items'][i]['name']
#         #   + " - " + fulldata[i]['track']['album']['name']
#         fancylist.append(entry)
#     pprint(fancylist)
#     print("=============================================")
#     fancylist = []
#     fulldata = sp.current_user_top_tracks(time_range='long_term')
#     # pprint(fulldata)
#     for i in range (20):  # using list1 doesn't work
#
#         # print(item['track']['artists'][0]['name']   + " - " + item['track']['name']  + " - " + item['track']['album']['name'])
#         entry = fulldata['items'][i]['artists'][0]['name']   + " - " + fulldata['items'][i]['name']
#         #   + " - " + fulldata[i]['track']['album']['name']
#         fancylist.append(entry)
#     pprint(fancylist)
#     print("=============================================    ")

# def current_func():
# fulldata = sp.audio_features("spotify:track:5VctLR5RDyzjkaFiNrxZNd")
#     pprint(fulldata)

    # fancylist = []
    # fulldata = sp.artist_top_tracks("spotify:artist:5fENlrINIVP0gJOtKxvORt")
    # pprint(fulldata)
    #
    # print(type(fulldata))
    # print(fulldata['tracks'][0]['name'])
    # dic = {}
    # spotify:track:5VctLR5RDyzjkaFiNrxZNd
    # for i in range (10):
    #     # dic = item
    #     entry = fulldata['tracks'][i]['name']
    #     fancylist.append(entry)
    # pprint(fancylist)

def synergize():
    testlist = "spotify:playlist:5NKYetvb0UeaSDcnjs7SB7"
    # use_purgelist()


    idlist = get_diff(utils.ROADKILL, "roadkill", utils.ROADKILL_REPO, "roadkill repo", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.ROADKILL_REPO)  # add tracks from roadkill to rkrepo
    idlist.clear()


    idlist = get_diff(utils.ROADKILL_REPO, "roadkill repo", utils.OMNI, "omniscience", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.OMNI)
    idlist.clear()

    idlist = get_diff(utils.OMNI, "omniscience", utils.OMNI_REPO, "omniscience omni", PlaylistGetTypes.IDS_ONLY)
    if idlist != []:
        add_tracks(idlist, utils.OMNI_REPO)
    idlist.clear()
    # idlist = get_diff(utils.ROADKILL, "Roadkill", utils.OMNI, "Omniscience", PlaylistGetTypes.IDS_ONLY)
    #
    # idlist = get_diff(utils.ROADKILL, "Roadkill", utils.OMNI, "Omniscience", PlaylistGetTypes.IDS_ONLY)

    # add_tracks(idlist, testlist)

