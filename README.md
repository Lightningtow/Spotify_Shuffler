# Spotify Shuffler
When you listen to Spotify with shuffle play enabled, it's not actually random.  
Spotify plays you songs in an order it thinks you'd like to hear. Unfortunately, this algorithm is not very good,
and it ends up just playing you the same 20 songs over and over again.

The way around this is to shuffle the playlist order, and then listen through the playlist with shuffle disabled.  


Note: Spotify's API does not let you add local tracks to playlists. 
At the moment, local tracks as well as podcasts will be removed from the playlist when shuffling in place. 
When creating new shuffled copies, the original playlist won't be changed, 
and the new shuffled playlist won't have local tracks or podcasts included.

## Setup:
1) First off, you'll need to register yourself as a Spotify developer and create an app. Don't worry, it sounds harder than it actually is. 
   1) To do this, see https://developer.spotify.com/documentation/web-api/concepts/apps
   2) Name it whatever you want. For the redirect URI, I'd recommend using `http://localhost:8080`, although many URLs work.
2) Provide your client id, client secret, and redirect URI. You generally only need to do this once.
3) Grant your new app permission to access your Spotify account.
4) Setup is done! It should automatically refresh your tokens as needed, with no further action required on your part.


## Running the app:
Note: This app requires an internet connection to work.

You can either shuffle the playlist in place, or create a new one.  

##### Shuffle in place:
The playlist's tracks will be rearranged, permanently. There's no way to get back the old order, so be certain you want to do this.    

##### Create new playlist:
Ceates a playlist that's a duplicate of the old one, except shuffled. 
             The description and cover art are carried over, and the title is the same but with `(shuffled)` appended.


###FAQ

##### I'm stuck on `authenticating in browser...`
That's because you have an invalid

##### How can I change the font size/appearance?

CMD -> settings. Under profiles -> defaults -> appearance