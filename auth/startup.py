from auth.flask_spotify_auth import getAuth, refreshAuth, getToken

#Add your client ID
# YOU SHOULD USE os.environ['CLIENT']
CLIENT_ID = "b0a2b9b464de4ec3bafad3e0707746ec"

#aDD YOUR CLIENT SECRET FROM SPOTIFY
# YOU SHOULD USE os.environ['SECRET']
CLIENT_SECRET = "07cec236f9d0439a9d95ffcc421b69b7"

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
