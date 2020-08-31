import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from auth import startup
import time

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

class RecentTrack(Track):
    def __init__(self, id, name, artist, imageUrl, popularity, played_at):
        Track.__init__(self, id, name, artist, imageUrl, popularity)
        self.played_at = played_at

class Playlist():
	def __init__(self, id, name, imageUrl, description):
		self.id = id
		self.name = name
		self.imageUrl = imageUrl
		self.description = description


        

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

	recent_track_list = list()
	track_ids = list()

	for item in recently_played:
		track_ids.append(item['track']['id'])

	tracks = spotifyObject.tracks(track_ids)
	tracks = tracks['tracks']
	
	i = 0
	for item in recently_played:
		p = item['played_at']
		p = p.split("T")
		played_at = [p[0], p[1][:-5]]
		recent_track = RecentTrack(item['track']['id'], item['track']['name'], item['track']['artists'][0]['name'], tracks[i]['album']['images'][0]['url'], tracks[i]['popularity'], played_at)
		recent_track_list.append(recent_track)
		i+=1
	return recent_track_list


#Return the most listend artists
#	limit: from 1 to 50
#	time_range: short_term (~1 month), medium_term (~6 months), long_term (all time)
def top_artists(spotifyObject, limit, time_range):
	top_artists = spotifyObject.current_user_top_artists(limit=limit, offset=0, time_range=time_range)
	top_artists = top_artists['items']

	artist_list = list()
	for item in top_artists:
		artist = Artist(item['name'],item['images'][0]['url'],item['popularity'])
		artist_list.append(artist)

	return artist_list


#Return the most played tracks
#	limit: from 1 to 50
#	time_range: short_term (~1 month), medium_term (~6 months), long_term (all time)
def top_tracks(spotifyObject, limit, time_range):
	top_tracks = spotifyObject.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)
	top_tracks = top_tracks['items']

	track_list = list()
	for item in top_tracks:
		track = Track(item['id'], item['name'], item['artists'][0]['name'], item['album']['images'][0]['url'], item['popularity'])
		track_list.append(track)

	return track_list


def user_playlists(spotifyObject):
	user_playlists = spotifyObject.current_user_playlists()
	user_playlists = user_playlists['items']

	playlist_list = list()
	for item in user_playlists:
		playlist = Playlist(item['id'], item['name'],item['images'][0]['url'], item['description'])
		playlist_list.append(playlist)

	return playlist_list


#print(json.dumps(user_playlists, sort_keys=True, indent=4))