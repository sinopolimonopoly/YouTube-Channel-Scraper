from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_videos_info(video_ids):
    # Defaultdict allows dictionary keys to be created while they are first being assigned
    # Calling videos["Hello"] Will create a new key 'Hello' with a value of an empty dictionary
        # -> {"Hello": {}}
    # Now, we can easily assign a new key to this inner dictionary
        # videos["Hello"]["key_1"] = "first value" -> {"Hello": {"key_1": "first_key"}}
    # With this data structure, we can have outer keys as video IDs, which have keys that are 
    # dictionaries containing key-value pairs of the video's attributes
    videos = defaultdict(dict)

    for list_type, ids in video_ids.items(): 

        # Videos can be searched for in batches of 50
        # 50 is the max search length and most effective use of api credits
        # If there are 125 video is, this loop will run three times
            # 0-49, 50-99, 100-149 (grabs the last 25 videos)
        for i in range(0, len(ids), 50):
            # Create a batch of the ith 50 videos
            # Remember that list slicing is not inclusive of the upper boundary
            # Also, the list slicing stop index can exceed the length of the list 
            batch = ids[i:i+50]

            # The IDs need to be passed in the api call as a comma separated list. This can be accomplished with the join method
            # Below will product a string of all the IDs in the batch list, separated by commas
            # '|'.join([111, 222, 333, 444]) -> "111|222|333|444"
            comma_separated_ids = ','.join(batch)

            # Note that this search is for videos
            # Retreive contentDetails, snippet and statistics parts for different attributes of the video
            # Pass the list of ids to search for
            url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet,statistics&id={comma_separated_ids}&key={api_key}"
            res = requests.get(url)
            data = res.json()

            for item in data['items']:
                try:
                    # Retrieve information from each video
                    # Snippet
                    video_id = item['id']
                    title = item['snippet']['title']
                    upload_date = item['snippet']['publishedAt'][0:10]

                    # Content Details
                    raw_duration = item['contentDetails']['duration'].replace("PT", "")
                    processed_duration = process_duration(raw_duration, item)

                    # Statistics
                    view_count = item['statistics']['viewCount']
                    # Handling cases where likes and comments are disabled
                    if "likeCount" in item['statistics']:
                        like_count = item['statistics']['likeCount']

                    else:
                        like_count = "Disabled"

                    if "commentCount" in item['statistics']:
                        comment_count = item['statistics']['commentCount']

                    else:
                        comment_count = "Disabled"

                    # Assign information to the video's dictionary
                    # Remember that the key is the video_id
                    videos[video_id]["Title"] = title
                    videos[video_id]["Upload Date"] = upload_date
                    videos[video_id]["Numeric Date"] = int("".join(upload_date.split('-')))
                    video_type = "Long Form" if (list_type == "videos") else "Short" if (list_type == "shorts") else "?"
                    videos[video_id]["Video Type"] = video_type

                    videos[video_id]["Duration"] = raw_duration
                    videos[video_id]["Duration in s"] = processed_duration    

                    videos[video_id]["View Count"] = view_count
                    videos[video_id]["Like Count"] = like_count
                    videos[video_id]["Comment Count"] = comment_count

                    # Dictionary addition of one video iteration:
                    # {"dQw4w9WgXcQ": {"Title": "Rick Astley - Never Gonna Give You Up (Official Music Video)", "Upload Date": "2009-10-25", ...}, ...}
                
                # Error handling if nonexistent key is pulled  from
                except KeyError as e:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(e)
                    print(f"Video Item: {item}")
                    exit()
        
    return videos

# To convert duration (2M30S) to seconds (150S) 
def process_duration(raw_duration, vid_item):

    try:  
        duration = raw_duration.replace("PT", "")

        if "D" in duration: #Video is long af (over 24 hours)
            return duration

        if "H" in duration:
            hour_idx = duration.index("H")
            hr_seconds = int(duration[0:hour_idx]) * 60 * 60
        
        else: 
            hr_seconds = 0
            hour_idx = -1

        if "M" in duration:
            minute_idx = duration.index("M")
            min_seconds = int(duration[hour_idx+1:minute_idx]) * 60

        else: 
            min_seconds = 0
            minute_idx = hour_idx


        if "S" in duration:
            sec_seconds = int(duration[minute_idx+1:-1])

        else:
            sec_seconds = 0

        duration_in_s = hr_seconds + min_seconds + sec_seconds

        return duration_in_s

    except ValueError as e:
        print(f"ValueError!")
        print(f"Video: {vid_item}")
        raise e
    