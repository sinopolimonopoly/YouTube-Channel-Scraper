from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

from output_scripts.make_csv_file import append_video_to_csv


load_dotenv()
api_key = os.getenv("API_KEY")

def get_videos_info(video_ids,handle):
    # Defaultdict allows dictionary keys to be created while they are first being assigned
    # Calling videos["Hello"] Will create a new key 'Hello' with a value of an empty dictionary
        # -> {"Hello": {}}
    # Now, we can easily assign a new key to this inner dictionary
        # videos["Hello"]["key_1"] = "first value" -> {"Hello": {"key_1": "first value"}}
    # With this data structure, we can have outer keys as video IDs, which have keys that are dictionaries containing key-value pairs of the video's attributes
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

            # The IDs need to be passed in the api call as a comma separated string. This can be accomplished with the join method
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

                # Reset variables every iteration
                title = None
                upload_date = None
                raw_duration = None
                processed_duration = None
                view_count = None
                like_count = None
                comment_count = None

                try:
                    # Retrieve information from each video
                    # Snippet
                    snippet = item.get("snippet") or {}
                    content_details = item.get("contentDetails") or {}

                    video_id = item.get("id")  # id is NOT inside snippet
                    title = snippet.get("title")

                    published_at = snippet.get("publishedAt")
                    upload_date = published_at[:10] if published_at else None

                    live_status = snippet.get("liveBroadcastContent")

                    # Content Details
                    if live_status == "live":
                        raw_duration = "Currently live"
                        processed_duration = "Currently live"

                    elif live_status == "upcoming":
                        continue

                    else:
                        duration = content_details.get("duration")

                        if duration:
                            raw_duration = duration.replace("P", "").replace("T", "")
                            processed_duration = process_duration(raw_duration, item)
                        else:
                            raw_duration = None
                            processed_duration = None 

                    # Statistics
                    statistics = item.get("statistics") or {}

                    view_count = statistics.get("viewCount")

                    like_count = statistics.get("likeCount")
                    comment_count = statistics.get("commentCount")

                    # Handle disabled likes/comments
                    like_count = like_count if like_count is not None else "Disabled"
                    comment_count = comment_count if comment_count is not None else "Disabled"

                  
                # Error handling if nonexistent key is pulled from
                except Exception as e:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(e)
                    print(f"Video Item: {item}")

                    title = title if title else None
                    upload_date = upload_date if upload_date else None
                    raw_duration = raw_duration if raw_duration else None
                    processed_duration = processed_duration if processed_duration else None
                    view_count = view_count if view_count else None
                    like_count = like_count if like_count else None
                    comment_count = comment_count if comment_count else None

                video_type = (
                    "Long Form" if list_type == "videos"
                    else "Short" if list_type == "shorts"
                    else "Livestream"
                )

                # Assign information to the video's dictionary
                # Remember that the key is the video_id
                append_video_to_csv({
                    "Video ID": video_id,
                    "Title": title,
                    "Upload Date": upload_date,
                    "Numeric Date": int("".join(upload_date.split('-'))),
                    "Video Type": video_type,

                    "Duration": raw_duration,
                    "Duration in s": processed_duration,

                    "View Count": view_count,
                    "Like Count": like_count,
                    "Comment Count": comment_count
                }, handle, video_type)

                # Dictionary addition of one video iteration:
                # {"dQw4w9WgXcQ": {"Title": "Rick Astley - Never Gonna Give You Up (Official Music Video)", "Upload Date": "2009-10-25", ...}, ...}
                


    print("Video Get ID Function Done Successfully") 
        
    return videos 

# To convert duration (2M30S) to seconds (150S) 
def process_duration(raw_duration, vid_item):

    try:  
        duration = raw_duration.replace("P", "").replace("T", "")

        if "D" in duration: #Video is long af (over 24 hours)
            day_idx = duration.index("D")
            day_seconds = int(duration[0:day_idx]) * 24 * 60 * 60

        else:
            day_seconds = 0
            day_idx = -1

        if "H" in duration:
            hour_idx = duration.index("H")
            hr_seconds = int(duration[day_idx+1:hour_idx]) * 60 * 60
        
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

        duration_in_s = day_seconds + hr_seconds + min_seconds + sec_seconds

        return duration_in_s

    except ValueError as e:
        print(f"ValueError!")
        print(f"Video: {vid_item}")
        raise e
    