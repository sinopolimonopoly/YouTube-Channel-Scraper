import sys
sys.stdout.reconfigure(encoding='utf-8')

from api_scripts.playlist_scripts.playlist_info_getter import get_playlist_info
from api_scripts.playlist_scripts.playlist_video_id_getter import get_playlist_video_ids
from api_scripts.playlist_scripts.playlist_video_info_getter import get_playlist_videos_info

playlist_id = "PL4J7fhM0o5VejAXLJJg2ZQul79fd68AnV"

playlist_info = get_playlist_info(playlist_id)

playlist_vid_ids = get_playlist_video_ids(playlist_id)

playlist_videos = get_playlist_videos_info(playlist_vid_ids)

print(playlist_videos)