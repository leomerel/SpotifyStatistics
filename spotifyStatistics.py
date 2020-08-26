import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from auth import startup

class Artist:
  def __init__(self, name, imageUrl, popularity):
    self.name = name
    self.popularity = popularity
    self.imageUrl = imageUrl

class Track:
	def __init__(self, id, name, artist, imageUrl, popularity):
		self.id = id
		self.name = name
		self.artist = artist
		self.imageUrl = imageUrl
		self.popularity = popularity

def connect():
	token= startup.getAccessToken() 

	# Create our spotify object with permissions
	spotifyObject = spotipy.Spotify(auth=token[0])

	# User information
	user = spotifyObject.current_user()
	userName = user['display_name']

	print("\nYou're connected to SpotifyStatistics with this account : " + userName + "\n")

	return spotifyObject


#Return the last 50 played tracks
def recently_played_tracks(spotifyObject):
	print("Last 50 played tracks: ")

	recently_played = spotifyObject.current_user_recently_played()
	recently_played = recently_played['items']

	track_list = list()
	z=1
	for item in recently_played:
	    track_list.append(str(z) + '. ' + 
	    	item['track']['artists'][0]['name'] +
	    	" - " + item['track']['name'] +
	    	" (" + item['played_at'] + ')')
	    z+=1

	return track_list


#Return the most listend artists
#	limit: from 1 to 50
#	time_range: short_term (~1 month), medium_term (~6 months), long_term (all time)
def top_artists(spotifyObject, limit, time_range):
	if time_range == 'short_term':
		print('Most played artists for the last  4 weeks: ')
	elif time_range == 'medium_term':
		print('Most played artists for the last 6 months: ')
	elif time_range == 'long_term':
		print('Most played artists of all time: ')

	top_artists = spotifyObject.current_user_top_artists(limit=limit, offset=0, time_range=time_range)
	top_artists = top_artists['items']

	artist_list = list()
	z=1
	for item in top_artists:
		artist = Artist(item['name'],item['images'][0]['url'],item['popularity'])
		artist_list.append(artist)
		z+=1

	return artist_list


#Return the most played tracks
#	limit: from 1 to 50
#	time_range: short_term (~1 month), medium_term (~6 months), long_term (all time)
def top_tracks(spotifyObject, limit, time_range):
	if time_range == 'short_term':
		print('Most played tracks for the last  4 weeks: ')
	elif time_range == 'medium_term':
		print('Most played tracks for the last 6 months: ')
	elif time_range == 'long_term':
		print('Most played tracks of all time: ')

	top_tracks = spotifyObject.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)
	top_tracks = top_tracks['items']

	track_list = list()
	z=1
	for item in top_tracks:
		track = Track(item['id'], item['name'], item['artists'][0]['name'], item['album']['images'][0]['url'], item['popularity'])
		track_list.append(track)
		z+=1

	return track_list