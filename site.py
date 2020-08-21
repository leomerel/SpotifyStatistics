import spotifyStatistics
from flask import Flask, redirect, url_for, render_template

spotifyObject = spotifyStatistics.connect()

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("homepage.html", artists=spotifyStatistics.top_artists(spotifyObject, 50, 'long_term'), title="Most played artists of all time")

if __name__ == "__main__":
	app.run()
