from bs4 import BeautifulSoup
import requests


date = input("Which year do you want to travel to? type date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}").text

soup = BeautifulSoup(response, "html.parser")

all_titles = soup.find_all(name="h3", class_="a-no-trucate")
 
titles = [title.getText().strip() for title in all_titles]

############################### Spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
 
CLIENT_ID = ""
CLIENT_SECRET = ""
URI = "http://example.com"
 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=URI,
                                               scope="playlist-modify-private",
                                             ))

# user-library-read
results = sp.current_user()
USER_ID = results['id']
# print(USER_ID) you will need user id to create a playlist and add tracks!
 
uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in titles]

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID, public=False, name=f"{date} BillBoard-100")['id']
 
sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID, tracks=uris, user=USER_ID)