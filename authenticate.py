import sys
import spotipy
import spotipy.util as util
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

scope = 'user-library-read user-top-read'
username = config['SPOTIFY']['username']
client_id=config['SPOTIFY']['client_id']
client_secret=config['SPOTIFY']['client_secret']
redirect_uri=config['SPOTIFY']['redirect_uri']

token = util.prompt_for_user_token(username, scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    print("authenticated")
else:
    print("No token")