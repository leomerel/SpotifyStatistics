import spotifyStatistics
from flask import Flask, redirect, url_for, render_template, request
from auth import startup

app = Flask(__name__)
global spotifyObject

#The first page, to connect to your spotify account
@app.route('/')
def index():
	response = startup.getUser()
	return redirect(response)

#The response redirects to /callback
#In the end, once we are successfully connected, we redirect to the homepage
@app.route('/callback/')
def callback():
	global spotifyObject
	startup.getUserToken(request.args['code'])
	spotifyObject = spotifyStatistics.connect()
	return redirect("http://127.0.0.1:5000/home", code=302)

@app.route("/home")
def home():
	return render_template("homepage.html")

@app.route("/topArtists")
def topArtists():
	return render_template("topArtists.html",
	 artists_4weeks=spotifyStatistics.top_artists(spotifyObject, 50, 'short_term'),
	 artists_6months=spotifyStatistics.top_artists(spotifyObject, 50, 'medium_term'),
	 artists_alltime=spotifyStatistics.top_artists(spotifyObject, 50, 'long_term'))

@app.route("/topTracks")
def topTracks():
	return render_template("topTracks.html",
	 tracks_4weeks=spotifyStatistics.top_tracks(spotifyObject, 50, 'short_term'),
	 tracks_6months=spotifyStatistics.top_tracks(spotifyObject, 50, 'medium_term'),
	 tracks_alltime=spotifyStatistics.top_tracks(spotifyObject, 50, 'long_term'))

@app.route("/recentlyPlayed")
def recentlyPlayed():
	return render_template("recentlyPlayed.html",
	 recentTracks=spotifyStatistics.recently_played_tracks(spotifyObject),
	 title="Recently played tracks")

if __name__ == "__main__":
	app.run()
