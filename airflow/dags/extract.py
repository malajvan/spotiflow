#export credentials before running spotipy
import subprocess
# subprocess.run(['bash', './start.sh'])
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date
print('extract.py: remember to run your start script to set environment variables')
def extract():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.playlist_tracks('37i9dQZF1DXcBWIGoYBM5M')
    # tracks = results['items']
    # while results['next']:
    #     results = spotify.next(results)
    #     tracks.extend(results['items'])
    tracks = []
    for tr in results['items']:
        tracks.append(tr['track'])


    track_ids = [track['id'] for track in tracks]

    # Fetch audio features for the track IDs
    audio_features = spotify.audio_features(track_ids)

    # Combine track information with audio features
    tracks_with_audio_features = []
    for i in range(len(tracks)):
        track_info = {
            'name': tracks[i]['name'],
            'artist': tracks[i]['artists'][0]['name'],
            'album': tracks[i]['album']['name'],
            'explicit': tracks[i]['explicit'],
            'duration_ms': tracks[i]['duration_ms'],
            'url': tracks[i]['external_urls']['spotify'],
            'extracted_date': date.today().strftime("%Y-%m-%d")
            # 'audio_features': audio_features[i]
        }
        merged = {**track_info, **audio_features[i]}
        del merged['track_href']
        del merged['type']
        del merged['analysis_url']
        del merged['uri']
        tracks_with_audio_features.append(merged)
    return tracks_with_audio_features
    # Save the data to a JSON file
    # with open('data.json', 'w') as json_file:
    #     json.dump(tracks_with_audio_features, json_file, indent=4)