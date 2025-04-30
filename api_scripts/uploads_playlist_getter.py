from dotenv import load_dotenv

from collections import defaultdict
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_uploads_playlist_id(channel_id, upload_type="all"):

    # Now that we have the channel's id, we can extract information about it
    # Specifically, we are retreiving the contentDetails part, which contans the playlist id for the channel's uploads
    ## url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={api_key}"

    ##res = requests.get(url)
    ##data = res.json()

    # Once again, the result is a list, but since the channel id was specified, there will only be one result
    # Therefore, access the first item
    # In the contentDetails object, access the relatedPlaylists object, and then the uploads value: which is the id of the playlist containing the videos
    ##playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    playlist_ids = defaultdict(str)

    # The playlist ID is identical to the channel id, except for the prefix
    # There are different prefixes 

    # Long form videos
    if upload_type == "videos":
        playlist_ids["videos"] = "UULF" + channel_id[2:]

    # Shorts
    elif upload_type == "shorts":
        playlist_ids["shorts"] = "UUSH" + channel_id[2:]

    # All uploads
    else:
        playlist_ids["videos"] = "UULF" + channel_id[2:]
        playlist_ids["shorts"] = "UUSH" + channel_id[2:]
        
    return playlist_ids
