import requests
import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_channel_id(handle):

    handle = handle.replace("@","")

    handle_verified = False

    # General endpoint is https://www.googleapis.com/youtube/v3/search
    # Part is always snippet
    # Type is what we're searching for, the channel
    # q is the search query, in this case, it is the channel handle
    # Key is the API key used to verify the request
    url = f"https://www.googleapis.com/youtube/v3/search?&part=snippet&type=channel&maxResults=50&q={handle}&key={api_key}"   

    res = requests.get(url)
    data = res.json()

    # The api call returns a response object, which should be converted to json to be processed as a Python dictionary
    # The result is actually a list of search results, but the first will be the one you care about, if you give the exact handle
    # Navigate to the id object of a search result, and extract the value of the channelId key. That will yield the correct channel ID
    for idx, item in enumerate(data['items']):
        try:
            channel_id = item["id"]["channelId"]
            handle_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,contentDetails&id={channel_id}&key={api_key}"
            res = requests.get(handle_url)
            channel_data = res.json()

            data_title = channel_data['items'][0]['snippet']['title']
            print(data_title)

            if " - Topic" in data_title:
                print("Topic channel found: ", data_title)
                continue

            data_handle = channel_data['items'][0]['snippet']['customUrl']

            if data_handle.lower().replace("@", "")== handle.lower():
                handle_verified = True
                valid_idx = idx
                break
        except KeyError:
            print(channel_data)

    
    if handle_verified:
        channel_id = data['items'][valid_idx]['id']['channelId']
        print(channel_id)
        return channel_id
    
    else:
        print(f"No channel with handle: {handle} found.")
        return

