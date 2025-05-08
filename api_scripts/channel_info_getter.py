from dotenv import load_dotenv

import os
import requests

from collections import defaultdict

load_dotenv()
api_key = os.getenv("API_KEY")

def get_channel_info(channel_id):

    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}"

    res = requests.get(url)
    data = res.json()

    channel_info = defaultdict(str)

    channel_info["Channel Name"] = data['items'][0]['snippet']['title']
    channel_info["Join Date"] = data['items'][0]['snippet']['publishedAt'][0:10]
    channel_info["Description"] = data['items'][0]['snippet']['description']
    channel_info["Handle"] = data['items'][0]['snippet']['customUrl']

    print(channel_info)