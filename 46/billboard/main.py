import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Constants
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""


def fetch_songs_and_artists(date: str) -> list[dict]:
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"An error occurred: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    artist_names_spans = soup.select("li ul li span.c-label.a-no-trucate.a-font-primary-s.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line.u-max-width-330")
    
    return [
        {'song': song.getText().strip(), 'artist': artist.getText().strip()}
        for song, artist in zip(song_names_spans, artist_names_spans)
    ]


def make_playlist(song_artist: list[dict], date: str) -> None:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri="http://example.com",
                                                   scope="playlist-modify-private"))
    
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100 {date}", public=False)
    playlist_id = playlist["id"]
    year = date.split("-")[0]
    uris = []
    for entry in song_artist:
        song = entry['song']
        artist = entry['artist']
        try:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            uris.append(result["tracks"]["items"][0]["uri"])
        except IndexError:
            logging.info(f"{song} by {artist} doesn't exist in Spotify. Skipped.")
    
    sp.playlist_add_items(playlist_id=playlist_id, items=uris)
    logging.info(f"Playlist created: https://open.spotify.com/playlist/{playlist_id}")


if __name__ == "__main__":
    date = "-".join([input(f"Enter a {time_unit}: ") for time_unit in ["year", "month", "day"]])
    song_artist = fetch_songs_and_artists(date)
    
    if song_artist:
        with open('billboard.json', 'w') as f:
            json.dump(song_artist, f, indent=4)
        
        make_playlist(song_artist, date)

