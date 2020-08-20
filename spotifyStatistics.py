import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

username = '21osyakzdl363eszq54vl5csy'
scope = 'user-read-recently-played user-top-read'

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
	print("Last 50 played tracks: ")

	recently_played = spotifyObject.current_user_recently_played()
	recently_played = recently_played['items']

	z=0
	for item in recently_played:
	    print(str(z) + '. ' + 
	    	item['track']['artists'][0]['name'] +
	    	" - " + item['track']['name'] +
	    	" (" + item['played_at'] + ')')
	    z+=1

	print("\n\n")


#Display the most listend artists
#	limit: from 1 to 50
#	time_range: short_term (~1 month), medium_term (~6 months), long_term (all time)
def top_artists(limit, time_range):
	if time_range == 'short_term':
		print('Most played artists for the last  4 weeks: ')
	elif time_range == 'medium_term':
		print('Most played artists for the last 6 months: ')
	elif time_range == 'long_term':
		print('Most played artists of all time: ')

	top_artists = spotifyObject.current_user_top_artists(limit=limit, offset=0, time_range=time_range)
	top_artists = top_artists['items']

	z=1
	for item in top_artists:
	    print(str(z) + '. ' + item['name'])
	    z+=1

	print("\n\n")


#Display the most played tracks
#	limit: from 1 to 50
#	time_range: short_term (~1 month), medium_term (~6 months), long_term (all time)
def top_tracks(limit, time_range):
	if time_range == 'short_term':
		print('Most played tracks for the last  4 weeks: ')
	elif time_range == 'medium_term':
		print('Most played tracks for the last 6 months: ')
	elif time_range == 'long_term':
		print('Most played tracks of all time: ')

	top_tracks = spotifyObject.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)
	top_tracks = top_tracks['items']

	#print(json.dumps(top_tracks, sort_keys=True, indent=4))

	z=1
	for item in top_tracks:
	    print(str(z) + '. ' + 
	    	item['name'] +
	    	" - " + item['artists'][0]['name'])
	    z+=1

	print("\n\n")



recently_played_tracks()
top_artists(50, 'long_term')
top_tracks(50, 'long_term')
