from dotenv import load_dotenv
from collections import defaultdict

import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_playlist_videos_info(video_ids):
    
    videos = defaultdict(dict)

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        comma_separated_ids = ','.join(batch)
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
                # If livestream is taking place right now
                if item['snippet']['liveBroadcastContent'] == "live":
                    raw_duration = "Currently live"
                    processed_duration = "Currently live"

                # skipping over upcoming livestreams
                elif item['snippet']['liveBroadcastContent'] == "upcoming":
                    continue

                else:
                    raw_duration = item['contentDetails']['duration'].replace("P", "").replace("T", "")
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

                videos[video_id]["Duration"] = raw_duration
                videos[video_id]["Duration in s"] = processed_duration    

                videos[video_id]["View Count"] = view_count
                videos[video_id]["Like Count"] = like_count
                videos[video_id]["Comment Count"] = comment_count


                # Dictionary addition of one video iteration:
                # {"dQw4w9WgXcQ": {"Title": "Rick Astley - Never Gonna Give You Up (Official Music Video)", "Upload Date": "2009-10-25", ...}, ...}
            
            # Error handling if nonexistent key is pulled from
            except KeyError as e:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(e)
                print(f"Video Item: {item}")
                exit()
            
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
    