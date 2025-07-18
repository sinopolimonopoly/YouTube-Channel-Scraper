from api_scripts.channel_id_getter import get_channel_id
from api_scripts.info.channel_info_getter import get_channel_info

# Channel to get info for
handle = "mrfruit"

# Get channel ID
channel_id = get_channel_id(handle)
# Output -> 'channel ID'

if not channel_id:
    print(f"No channel found for handle: {handle}")
    exit()

# Get channel info
channel_info = get_channel_info(channel_id)
print(channel_info)

