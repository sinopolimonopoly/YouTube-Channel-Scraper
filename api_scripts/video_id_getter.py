from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_video_ids(playlists, max_results=50):

    if max_results < 1 or max_results > 50:
        raise Exception("Enter a results value between 1 and 50.")

    # A list to store all of the video ids
    video_ids = defaultdict(list)
    # To paginate through results if there are more than 50 items in the playlist
    next_page_token = None

    for vid_type, playlist in playlists.items():
        type_ids = []
        while True:
            # With the playlist ID, retrieve the snippet for a search of 50 (max_results) videos
            # The request will continue to update and gather new videos beyond the first 50 with the page token
            # Note that the search is now for playlistItems
            url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={max_results}&playlistId={playlist}&key={api_key}"

            # The result will contain a nextPageToken key if there is another page of results to fetch
            # On the first run of the loop, next_page_token is undefined, so this will skip
            if next_page_token:
                # Add the page token to the api request to ensure the right page is being accessed
                url += f"&pageToken={next_page_token}"

            res = requests.get(url)
            data = res.json()
            
            # Error handling for API Call
            # If a channel has no shorts or long form videos, the request will yield an error
            if 'error' in data:
                # Get video type that failed
                current_type = "Long Form" if vid_type == "videos" else "Shorts" if vid_type == "shorts" else "Livestreams" if vid_type == "livestreams" else "INVALID VIDEO TYPE"
                print(f"{vid_type} | Can't retrieve {current_type}. The desired playlist may be empty")

                # Move on to next video type (next iteration in loop)
                break

            # Now, we need to iterate through all of the items in the search in order to look at each videos
            for item in data['items']:

                if vid_type == "videos" or vid_type == "shorts":
                    # Live streams are weird, and might want to be excluded
                    # https://www.youtube.com/watch?v=7jIkNN_OK1E for example
                    thumbnail_url = item['snippet']['thumbnails']['default']['url']
                    # Streams have different thumbnail urls (most times)
                    if "default_live.jpg" in thumbnail_url:
                        continue # Skip over the current video
                    
                # Retrieve the videoID value within the snippet and resourceId objects
                video_id = item['snippet']['resourceId']['videoId']
                # Add the video id to the list
                type_ids.append(video_id)
            
            # Retrieve the next page token to add to the next api call
            next_page_token = data.get('nextPageToken')

            # On the last page, there will be non nextPageToken key in the api response
            # If next_page_token evaluates to None, the following if statement will execute, ending the loop
            if not next_page_token:
                break

        video_ids[vid_type] = type_ids

    return video_ids
