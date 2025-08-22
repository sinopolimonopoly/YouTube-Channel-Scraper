import sys
sys.stdout.reconfigure(encoding='utf-8')

from api_scripts.channel_id_getter import get_channel_id
from api_scripts.uploads_playlist_getter import get_uploads_playlist_id
from api_scripts.video_id_getter import get_video_ids
from api_scripts.video_info_getter import get_videos_info
from output_scripts.info_outputter import output_info
from output_scripts.dict_to_csv import create_video_csv

# Channel to scrape
handle = "AsumSaus"
# videos (long form), shorts, livestreams, all_uploads 
video_type = "all_uploads"

# Get channel ID
channel_id = get_channel_id(handle)
# Output -> 'channel ID'

if not channel_id:
    print(f"No channel found for handle: {handle}")
    exit()

# Get playlist ID of the channel's videos
channel_uploads_playlist = get_uploads_playlist_id(channel_id, video_type)
# Output -> {'video type': 'playlist ID'}

# Get the ids of all the videos in the playlist(s)
video_ids = get_video_ids(channel_uploads_playlist)
# Output {'video type': [List of ids]}
print(video_ids)

# Get the information for each video
video_info = get_videos_info(video_ids)
# Output {'Video ID': {'Title': 'My Video', 'Upload Date': '2025-04-30', ...}, ...}

# Sorting videos by date uploaded
# Needed because shorts and uploads are separated
# item is a key value pair, index 1 is the value, 'Numeric Date' is the desired sorting attribute
videos_by_date = dict(sorted(video_info.items(), key = lambda item: item[1]['Numeric Date'], reverse=True))
# print(videos_by_date)
# Output to console and create csv file, if request went through
if bool(video_info) == True: # if dictionary contains something
    # Output the dictionary to the console (in a table)
    output_info(videos_by_date)

    # Create CSV file for dictionary, if valid dictionary
    create_video_csv(videos_by_date, handle, video_type)

else:
    print(f"No output. {video_type} request for channel {handle} yielded empty dictionary")