from api_scripts.channel_id_getter import get_channel_id
from api_scripts.uploads_playlist_getter import get_uploads_playlist_id
from api_scripts.video_id_getter import get_video_ids
from api_scripts.video_info_getter import get_videos_info

from output_scripts.info_outputter import output_info
from output_scripts.dict_to_csv import create_video_csv

handle = "curtisdoingthings"

channel_id = get_channel_id(handle)

channel_uploads_playlist = get_uploads_playlist_id(channel_id)

video_ids = get_video_ids(channel_uploads_playlist, 50)

video_info = get_videos_info(video_ids)

output_info(video_info)
create_video_csv(video_info)