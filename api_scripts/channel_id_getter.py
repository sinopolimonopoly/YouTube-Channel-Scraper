import requests
import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_channel_id(handle):

    # General endpoint is https://www.googleapis.com/youtube/v3/search
    # Part is always snippet
    # Type is what we're searching for, the channel
    # q is the search query, in this case, it is the channel handle
    # Key is the API key used to verify the request
    url = f"https://www.googleapis.com/youtube/v3/search?&type=channel&q={handle}&key={api_key}"

    res = requests.get(url)
    data = res.json()

    # The api call returns a response object, which should be converted to json to be processed as a Python dictionary
    # The result is actually a list of search results, but the first will be the one you care about, if you give the exact handle
    # Navigate to the id object of a search result, and extract the value of the channelId key. That will yield the correct channel ID
    channel_id = data['items'][0]['id']['channelId']

    return channel_id

