from api_scripts.channel_id_getter import get_channel_id
from api_scripts.uploads_playlist_getter import get_uploads_playlist_id
from api_scripts.video_id_getter import get_video_ids
from api_scripts.video_info_getter import get_videos_info

from output_scripts.info_outputter import output_info
from output_scripts.dict_to_csv import create_video_csv

# Channel to scrape
handle = "FeinbergMC"

# Get channel ID
channel_id = get_channel_id(handle)

# Get playlist ID of all of channel's uploads
channel_uploads_playlist = get_uploads_playlist_id(channel_id)

# Get all of the video IDs
video_ids = get_video_ids(channel_uploads_playlist, 50)

# Get information from each video
video_info = get_videos_info(video_ids)

# Output the dictionary to the console (in a table)
output_info(video_info)
# Create CSV file of dictionary
create_video_csv(video_info, handle)