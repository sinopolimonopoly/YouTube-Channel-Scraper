from api_scripts.channel_id_getter import get_channel_id
from api_scripts.uploads_playlist_getter import get_uploads_playlist_id
from api_scripts.new_id_getter import get_video_ids
from api_scripts.new_info_getter import get_videos_info
from output_scripts.info_outputter import output_info
from output_scripts.dict_to_csv import create_video_csv

# Channel to scrape
handle = "dudeperfect"
# videos (long form), shorts, all_uploads 
video_type = "all_uploads"

# Get channel ID
channel_id = get_channel_id(handle)

# Get playlist ID of all of channel's uploads
channel_uploads_playlist = get_uploads_playlist_id(channel_id, video_type)
# Get the information of all the videos in the playlists
video_ids = get_video_ids(channel_uploads_playlist)

video_info = get_videos_info(video_ids)

videos_by_date = dict(sorted(video_info.items(), key = lambda item: item[1]['Numeric Date'], reverse=True))
# Output the dictionary to the console (in a table)
output_info(videos_by_date)
# Create CSV file of dictionary
create_video_csv(videos_by_date, handle, video_type)