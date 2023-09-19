#export credentials before running spotipy
import subprocess
subprocess.run(['bash', './start.sh'])

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.playlist_tracks('37i9dQZF1DXcBWIGoYBM5M')
tracks = results['items']
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])


for idx, track in enumerate(tracks, start=1):
    track_name = track['track']['name']
    artists = ', '.join(artist['name'] for artist in track['track']['artists'])
    print(f"{idx}. {track_name} - {artists}")