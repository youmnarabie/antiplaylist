import spotipy
import sys
import discogs_client
import spotipy.oauth2 as oauth2
import spotipy.util as util
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getAnti(artist):
	artist_genres = artist.get("artists").get("items")[0].get('genres')
    most_common_genre = np.random.choice(artist_genres).replace(" ", "").replace("-", "")
    print(most_common_genre)
    quote_page = 'http://everynoise.com/engenremap-'+ most_common_genre + '.html'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    holder = list()
    if most_common_genre in antis.keys():
    	holder = antis.get(most_common_genre)
    else: 
        for div in soup.findAll('div', attrs={'id':'mirror'}):
            holder.extend(div.text.replace("»", "").strip().split("\n"))
        antis[most_common_genre] = holder
    curr_anti = np.random.choice(antis.get(most_common_genre)).replace(" ", "").replace("-", "")
    return curr_anti
#url = sys.argv
url = input("Paste Playlist URL\n")
type(url)


split_url = url.split("/")

playlist_info = split_url[6]
id_end_index = playlist_info.find("?")

playlist_id = playlist_info[:id_end_index]
username = split_url[4]

client_id = '70ce61b3518c4b68a9b583e1f9e971b4'
client_secret = '36b26da39113479dac1f38743ada505f'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token = util.prompt_for_user_token(username, scope="playlist-read-private", client_id=client_id, client_secret=client_secret, redirect_uri='https://example.com/callback/')
#token = generate_token()
if token:
    #sp = spotipy.Spotify(auth=token)
    results = spotify.user_playlist(username, playlist_id)
    songs = results["tracks"]
    # List of song ids 
    ids = list()
    # List of artist objects
    artists = list()
    # List of search results from which genres are to be extracted 
    genres = list()
    # List of artist names
    names = list()
    # Dictionary of genres : list of anti-genres 
    antis = dict() 


    #Find a list of all track ids in the playlist 
    for i, item in enumerate(songs["items"]):
        song = item["track"]
        ids.append(song["id"])
        artists.append(song["artists"])
    # If there are more pages of songs, add them too. 
    while songs['next']:
        songs = sp.next(songs)
        for i, item in enumerate(songs["items"]):
            song = item["track"]
            ids.append(song["id"])
            artists.append(song["artists"])


    # List of track objects
    all_tracks = spotify.tracks(ids)
    # Find each artist's name for later searching
    for artist in artists:
    	names.append(artist[0].get("name"))

    # Search for every artist's name and append the name to "genres"
    for name in names: 
    	genre = spotify.search(name, limit = 1, type="artist")
    	genres.append(genre)

   	# Find the actual genre of every item in genres 
    for artist in genres:
    	# Remove the 0 to get a list of the artist's genres instead of just the first one 
        # artist_genres = artist.get("artists").get("items")[0].get('genres')
        # most_common_genre = np.random.choice(artist_genres).replace(" ", "").replace("-", "")
        # print(most_common_genre)
        # quote_page = 'http://everynoise.com/engenremap-'+ most_common_genre + '.html'
        # page = urlopen(quote_page)
        # soup = BeautifulSoup(page, 'html.parser')
        # holder = list()
        # if most_common_genre in antis.keys():
        # 	holder = antis.get(most_common_genre)
        # else: 
        #     for div in soup.findAll('div', attrs={'id':'mirror'}):
        #         holder.extend(div.text.replace("»", "").strip().split("\n"))
        #     antis[most_common_genre] = holder
        # curr_anti = np.random.choice(antis.get(most_common_genre)).replace(" ", "").replace("-", "")
        # print(curr_anti)
        curr_anti = getAnti(artist)


        # Go to anti page and find a random artist 
        quote_page = 'http://everynoise.com/engenremap-'+ curr_anti + '.html'
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        anti_artists = list()
        for div in soup.findAll('div', attrs={"class": "canvas"}):
        	anti_artists.extend(div.text.replace("»", "").strip().split("\n"))

        selected_anti = np.random.choice(anti_artists)
        print(selected_anti)
        anti_object = spotify.search(selected_anti, limit = 1, type="artist")
        anti_artistoo = anti_object.get("artists").get("items")
        anti_artist_id = ""
        for i in range(100): 
        	if len(anti_artistoo) == 0: 
        		selected_anti = np.random.choice(anti_artists)
        		anti_object = spotify.search(selected_anti, limit = 1, type="artist")
        	else:
        		break	
        else: 
        	anti_artist_id = anti_artistoo[0].get("id")
        print(anti_artist_id)
        top10 = spotify.artist_top_tracks(anti_artist_id)
        print(top10.get("tracks"))
        top10songs = list()
        #for song in top10.get("tracks"):
        	#print(song)
        	#break
        	#top10songs.append(song.get("name"))
       	#print(top10songs)


else:
    print("Can't get token for", username)

#{'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1CPB6Dveuoj02QW0P5khxq'}, 'href': 'https://api.spotify.com/v1/artists/1CPB6Dveuoj02QW0P5khxq', 'id': '1CPB6Dveuoj02QW0P5khxq', 'name': 'Clay Foster & Carey Frank', 'type': 'artist', 'uri': 'spotify:artist:1CPB6Dveuoj02QW0P5khxq'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/3x7D14dsBJeHLvmKFMEZrK'}, 'href': 'https://api.spotify.com/v1/albums/3x7D14dsBJeHLvmKFMEZrK', 'id': '3x7D14dsBJeHLvmKFMEZrK', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/bdb219ec451d204903238838a340a28da1dcd04a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/fece80f13450f78334ad629dd0620f585348ebe1', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/5ca55a0c5163cd883ae65f334dbbe40988fd99b0', 'width': 64}], 'name': 'Bona Fide Sea Monsters', 'release_date': '2011-01-21', 'release_date_precision': 'day', 'total_tracks': 8, 'type': 'album', 'uri': 'spotify:album:3x7D14dsBJeHLvmKFMEZrK'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1CPB6Dveuoj02QW0P5khxq'}, 'href': 'https://api.spotify.com/v1/artists/1CPB6Dveuoj02QW0P5khxq', 'id': '1CPB6Dveuoj02QW0P5khxq', 'name': 'Clay Foster & Carey Frank', 'type': 'artist', 'uri': 'spotify:artist:1CPB6Dveuoj02QW0P5khxq'}], 'disc_number': 1, 'duration_ms': 581605, 'explicit': False, 'external_ids': {'isrc': 'uscgh1100321'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/0LYRYs86HrZjLvw57L2Yuz'}, 'href': 'https://api.spotify.com/v1/tracks/0LYRYs86HrZjLvw57L2Yuz', 'id': '0LYRYs86HrZjLvw57L2Yuz', 'is_local': False, 'is_playable': True, 'name': 'Ratio Tensions', 'popularity': 0, 'preview_url': 'https://p.scdn.co/mp3-preview/d04f2e98defa48c5d2e081f3a1b5109fd5c80453?cid=70ce61b3518c4b68a9b583e1f9e971b4', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:0LYRYs86HrZjLvw57L2Yuz'}



