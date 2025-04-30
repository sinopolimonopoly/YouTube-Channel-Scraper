from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def get_videos_info(video_ids, max_duration=False):
    videos = defaultdict(lambda: defaultdict(dict))

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]

        url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet,statistics&id={','.join(batch)}&key={api_key}"
        res = requests.get(url).json()

        for item in res['items']:
            raw_duration = item['contentDetails']['duration'].replace("PT", "")

            if max_duration:
                processed_duration = process_duration(raw_duration, item)

                if processed_duration > max_duration:
                    continue

            # Get video information
            # Snippet
            video_id = item['id']
            title = item['snippet']['title']
            upload_date = item['snippet']['publishedAt'][0:10]

            # Statistics
            view_count = item['statistics']['viewCount']
            like_count = item['statistics']['likeCount']
            comment_count = item['statistics']['commentCount']

            videos[video_id]["Information"]["Title"] = title
            videos[video_id]["Information"]["Upload Date"] = upload_date

            if max_duration:
                videos[video_id]["Information"]["Duration"] = {"min_sec": raw_duration, "secs" : processed_duration}

            else:
                videos[video_id]["Information"]["Duration"] = raw_duration
            
            videos[video_id]["Statistics"]["View Count"] = view_count
            videos[video_id]["Statistics"]["Like Count"] = like_count
            videos[video_id]["Statistics"]["Comment Count"] = comment_count
        
    return videos


def process_duration(raw_duration, vid_item):

    try:  
        duration = raw_duration.replace("PT", "")

        if "M" in duration:
            minute_idx = duration.index("M")
            min_seconds = int(duration[0:minute_idx]) * 60

            if "S" in duration:
                leftover_seconds = int(duration[minute_idx+1:len(duration)-1])
                duration_in_s = min_seconds + leftover_seconds

            else:
                duration_in_s = min_seconds

        else:
            duration_in_s = int(duration[0:-1]) 

        return duration_in_s

    except ValueError as e:
        print(f"ValueError!")
        print(f"Video: {vid_item}")
        raise e