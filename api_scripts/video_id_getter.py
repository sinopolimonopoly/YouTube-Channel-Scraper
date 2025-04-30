from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_video_ids(playlist_id,max_results):

    counter = 0

    if max_results < 1 or max_results > 50:
        raise Exception("Enter a results value between 1 and 50.")

    video_ids=[]
    next_page_token = None

    while True:
        
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={max_results}&playlistId={playlist_id}&key={api_key}"

        if next_page_token:
            url += f"&pageToken={next_page_token}"

        res = requests.get(url).json()
        for item in res['items']:
            
            thumbnail_url = item['snippet']['thumbnails']['default']['url']
            title = item['snippet']['title']
            if "default_live.jpg" in thumbnail_url or "🔴" in title:
                continue

            video_id = item['snippet']['resourceId']['videoId']
            video_ids.append(video_id)
        
        next_page_token = res.get('nextPageToken')

        if not next_page_token:
            break

        counter += 1

        if counter > 50:
           break

    return video_ids

