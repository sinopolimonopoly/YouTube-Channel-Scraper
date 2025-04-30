from dotenv import load_dotenv

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_uploads_playlist_id(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={api_key}"
    res = requests.get(url).json()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return playlist_id
