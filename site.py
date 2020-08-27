import spotifyStatistics
from flask import Flask, redirect, url_for, render_template, request
from auth import startup
from auth.flask_spotify_auth import refreshAuth

app = Flask(__name__)
global spotifyObject
global logoutInProgress
logoutInProgress = False

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
	global logoutInProgress
	startup.getUserToken(request.args['code'])
	spotifyObject = spotifyStatistics.connect()
	if logoutInProgress==True:
		logoutInProgress=False
		return redirect("http://127.0.0.1:5000/", code=302)
	else:
		return redirect("http://127.0.0.1:5000/home", code=302)

@app.route("/logoutInProgress")
def logoutInProgress():
	return render_template("logout.html")

@app.route("/logout")
def logout():
	global logoutInProgress
	logoutInProgress = True
	response = startup.getUser()
	return redirect(response)

@app.route("/home")
def home():
	return render_template("homepage.html")

@app.route("/topArtists")
def topArtists():
	global spotifyObject
	return render_template("topArtists.html",
	 artists_4weeks=spotifyStatistics.top_artists(spotifyObject, 50, 'short_term'),
	 artists_6months=spotifyStatistics.top_artists(spotifyObject, 50, 'medium_term'),
	 artists_alltime=spotifyStatistics.top_artists(spotifyObject, 50, 'long_term'))

@app.route("/topTracks")
def topTracks():
	global spotifyObject
	return render_template("topTracks.html",
	 tracks_4weeks=spotifyStatistics.top_tracks(spotifyObject, 50, 'short_term'),
	 tracks_6months=spotifyStatistics.top_tracks(spotifyObject, 50, 'medium_term'),
	 tracks_alltime=spotifyStatistics.top_tracks(spotifyObject, 50, 'long_term'))

@app.route("/recentlyPlayed")
def recentlyPlayed():
	global spotifyObject
	return render_template("recentlyPlayed.html",
	 recentTracks=spotifyStatistics.recently_played_tracks(spotifyObject))


@app.route("/charts")
def charts():
	return render_template("charts.html", playlists = spotifyStatistics.user_playlists(spotifyObject))

if __name__ == "__main__":
	app.run()
