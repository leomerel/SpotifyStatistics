from auth.flask_spotify_auth import getAuth, refreshAuth, getToken
from dotenv import load_dotenv
import os

load_dotenv()

#Add your client ID
# YOU SHOULD USE os.environ['CLIENT']
CLIENT_ID = "b0a2b9b464de4ec3bafad3e0707746ec"

#Get your client SECRET from the environment variable you set
try:
    CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
except KeyError as e:
	print("/!\   Your client SECRET has to be set !             /!\ ")
	print("/!\   Use this command to set it:                    /!\ ")
	print("/!\           export SPOTIPY_CLIENT_SECRET=' ... '   /!\ ")


#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "user-read-recently-played user-top-read"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))

def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA
