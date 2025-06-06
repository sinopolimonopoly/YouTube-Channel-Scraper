import sys
sys.stdout.reconfigure(encoding='utf-8')

from api_scripts.playlist_scripts.playlist_info_getter import get_playlist_info
from api_scripts.playlist_scripts.playlist_video_id_getter import get_playlist_video_ids
from api_scripts.playlist_scripts.playlist_video_info_getter import get_playlist_videos_info

from output_scripts.info_outputter import output_info

playlist_id = "PL3SpvjWjivWbMCGQ5junh1In_CSwycqv4"

playlist_info = get_playlist_info(playlist_id)
print(playlist_info)

playlist_vid_ids = get_playlist_video_ids(playlist_id)

playlist_videos = get_playlist_videos_info(playlist_vid_ids)

#output_info(playlist_videos, True)