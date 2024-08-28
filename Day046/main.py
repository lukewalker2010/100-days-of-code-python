import requests
from bs4 import BeautifulSoup
import keys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL_BASE = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = keys.CLIENT_ID
CLIENT_SECRET = keys.CLIENT_SECRET
REDIRECT_URI = keys.REDIRECT_URI

date = input("Which year do you want to travel to? Tyep the date in this format YYYY-MM-DD: ")

url = URL_BASE + date

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Playlist created: {playlist['name']}")
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"{len(song_uris)} songs added to the playlist.")