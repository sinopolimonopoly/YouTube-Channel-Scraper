from api_scripts.channel_id_getter import get_channel_id
from api_scripts.info.channel_info_getter import get_channel_info
from output_scripts.channels_info_csv import make_channels_csv

from collections import defaultdict

one_or_multi = input("1 for one channel, 2 for multiple ")

# Channel to get info for
handle = "torontoraptors"
handles = ["torontomapleleafs", "torontoraptors", "torontofc", "torontoargonauts", "marliestv", "raptors905", "raptorsuprisinggc", "scotiabankarena", "mlsesportdevelopment", "mlsefoundation", "mlselaunchpad7987", "realsportsmlsq", "nbatvcanada"]



if int(one_or_multi) == 1:
    # Get channel ID
    channel_id = get_channel_id(handle)
    # Output -> 'channel ID'

    if not channel_id:
        print(f"No channel found for handle: {handle}")
        exit()

    # Get channel info
    channel_info = get_channel_info(channel_id)
    print(channel_info['Channel Name'], "done")
    
elif int(one_or_multi) == 2:
    print("asndkjasndjkahsd")
    results = []

    for handle in handles:
        channel_id = get_channel_id(handle)

        if not channel_id:
            print(f"No channel found for handle: {handle}")
            exit()

        # Get channel info
        channel_info = get_channel_info(channel_id)
        print(channel_info['Sub Count'])

        results.append(channel_info)

    print(results)
    make_channels_csv(results)
