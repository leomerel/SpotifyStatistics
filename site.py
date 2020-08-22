import spotifyStatistics
from flask import Flask, redirect, url_for, render_template

spotifyObject = spotifyStatistics.connect()

app = Flask(__name__)

@app.route("/home")
def home():
	return render_template("homepage.html",
	 artists=spotifyStatistics.top_artists(spotifyObject, 50, 'long_term'),
	 title1="Most played artists of all time",
	 tracks=spotifyStatistics.top_tracks(spotifyObject, 50, 'long_term'),
	 title2="Most played tracks of all time",
	 recentTracks=spotifyStatistics.recently_played_tracks(spotifyObject),
	 title3="Recently played tracks")

@app.route("/topArtists")
def topArtists():
	return render_template("topArtists.html",
	 artists_4weeks=spotifyStatistics.top_artists(spotifyObject, 50, 'short_term'),
	 artists_6months=spotifyStatistics.top_artists(spotifyObject, 50, 'medium_term'),
	 artists_alltime=spotifyStatistics.top_artists(spotifyObject, 50, 'long_term'))

@app.route("/topTracks")
def topTracks():
	return render_template("topTracks.html",
	 tracks=spotifyStatistics.top_tracks(spotifyObject, 50, 'long_term'),
	 title="Most played tracks of all time")

@app.route("/recentlyPlayed")
def recentlyPlayed():
	return render_template("recentlyPlayed.html",
	 recentTracks=spotifyStatistics.recently_played_tracks(spotifyObject),
	 title="Recently played tracks")

if __name__ == "__main__":
	app.run()
