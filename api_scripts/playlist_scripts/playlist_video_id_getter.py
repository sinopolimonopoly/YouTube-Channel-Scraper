from dotenv import load_dotenv

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_playlist_video_ids(playlist):

    # A list to store all of the video ids
    video_ids = []
    # To paginate through results if there are more than 50 items in the playlist
    next_page_token = None

    while True:
        # With the playlist ID, retrieve the snippet for a search of 50 (max_results) videos
        # The request will continue to update and gather new videos beyond the first 50 with the page token
        # Note that the search is now for playlistItems
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist}&key={api_key}"

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
            print("Error with api call")
            print(data['error']['message'])

            # Move on to next video type (next iteration in loop)
            return

        # Now, we need to iterate through all of the items in the search in order to look at each videos
        for item in data['items']:

            # Unavailable video in playlist
            if item['snippet']['title'] == "Deleted Video" and item['snippet']['description'] == "This video is unavailable.":
                #Move on to next video
                continue 
                
            # Retrieve the videoID value within the snippet and resourceId objects
            video_id = item['snippet']['resourceId']['videoId']
            # Add the video id to the list
            video_ids.append(video_id)
        
        # Retrieve the next page token to add to the next api call
        next_page_token = data.get('nextPageToken')

        # On the last page, there will be non nextPageToken key in the api response
        # If next_page_token evaluates to None, the following if statement will execute, ending the loop
        if not next_page_token:
            break

    return video_ids
