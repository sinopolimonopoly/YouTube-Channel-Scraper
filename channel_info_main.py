from api_scripts.channel_id_getter import get_channel_id
from api_scripts.info.channel_info_getter import get_channel_info

# Channel to get info for
handle = "AsumSaus"

# Get channel ID
channel_id = get_channel_id(handle)
# Output -> 'channel ID'

# Get channel info
channel_info = get_channel_info(channel_id)

