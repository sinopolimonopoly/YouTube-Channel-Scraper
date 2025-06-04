from dotenv import load_dotenv

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_playlist_info(playlist):
    url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet,contentDetails&id={playlist}&key={api_key}"

    res = requests.get(url)
    data = res.json()

    if data["pageInfo"]["totalResults"] == 0:
        print(f"No playlist found with id ${playlist}")
        return

    playlist_title = data['items'][0]["snippet"]["title"]
    playlist_description = data['items'][0]["snippet"]["description"]
    playlist_create_date = data['items'][0]["snippet"]["publishedAt"][0:10]
    playlist_channel = data['items'][0]["snippet"]["channelTitle"]
    playlist_video_count = data['items'][0]["contentDetails"]["itemCount"]

    return {
        "title": playlist_title,
        "description": playlist_description,
        "create_date": playlist_create_date,
        "channel" : playlist_channel,
        "video_count": playlist_video_count
        }
    

