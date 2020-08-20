import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

username = '21osyakzdl363eszq54vl5csy'
scope = 'user-read-recently-played'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# User information
user = spotifyObject.current_user()
userName = user['display_name']

print("\nYou're connected to SpotifyStatistics with this account : " + userName + "\n")


#Display the last 50 played tracks
def recently_played_tracks():
	recently_played = spotifyObject.current_user_recently_played()
	recently_played = recently_played['items']

	z=0
	for item in recently_played:
	    print(str(z) + '. ' + 
	    	item['track']['artists'][0]['name'] +
	    	" - " + item['track']['name'] +
	    	" (" + item['played_at'] + ')')
	    z+=1


recently_played_tracks()
