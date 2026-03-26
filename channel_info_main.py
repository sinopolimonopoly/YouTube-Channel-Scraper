from api_scripts.channel_id_getter import get_channel_id
from api_scripts.info.channel_info_getter import get_channel_info
from output_scripts.channels_info_csv import make_channels_csv

import argparse
import csv
import os


def upsert_channels_csv(channel_dict_list, output_folder="channel_output", file_name="channels_master.csv"):
    os.makedirs(output_folder, exist_ok=True)
    file_path = os.path.join(output_folder, file_name)

    fieldnames = [
        "Handle",
        "Channel ID",
        "Channel Name",
        "Join Date",
        "Description",
        "Thumbnail URL",
        "Subscriber Count",
        "View Count",
        "Video Count",
    ]

    existing_rows = {}
    if os.path.exists(file_path):
        with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                handle = row.get("Handle", "").strip()
                if handle:
                    existing_rows[handle] = row

    for channel_dict in channel_dict_list:
        handle = channel_dict.get("Handle", "").strip()
        if not handle:
            continue

        existing_rows[handle] = {
            "Handle": handle,
            "Channel ID": channel_dict.get("Channel ID", ""),
            "Channel Name": channel_dict.get("Channel Name", ""),
            "Join Date": channel_dict.get("Join Date", ""),
            "Description": channel_dict.get("Description", ""),
            "Thumbnail URL": channel_dict.get("Thumbnail URL", ""),
            "Subscriber Count": channel_dict.get("Sub Count", ""),
            "View Count": channel_dict.get("View Count", ""),
            "Video Count": channel_dict.get("Video Count", ""),
        }

    with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for handle in sorted(existing_rows.keys()):
            writer.writerow(existing_rows[handle])

    print(f"Updated {file_path} ({len(existing_rows)} unique handles)")


parser = argparse.ArgumentParser()
parser.add_argument(
    "--export-file",
    default="channels_master.csv",
    help="Optional custom export filename (default: channels_master.csv)",
)
args = parser.parse_args()

one_or_multi = input("1 for one channel, 2 for multiple ")

# Channel to get info for
handle = "WashingtonWizards"
handles = ["ATLHawks",
"Celtics",
"brooklynnets",
"hornets",
"ChicagoBulls",
"cavs",
"mavericks",
"DenverNuggets",
"PistonsTV",
"warriors",
"OfficialRockets",
"pacers",
"laclippers",
"lakers",
"MemphisGrizzlies",
"MiamiHEAT",
"bucks",
"timberwolves",
"NBAPelicans",
"NYKnicks",
"okcthunder",
"OrlandoMagic",
"sixers",
"Suns",
"trailblazers",
"SacramentoKings",
"spurs",
"torontoraptors",
"utahjazz",
"WashingtonWizards"]


if int(one_or_multi) == 1:
    # Get channel ID
    channel_id = get_channel_id(handle)
    # Output -> 'channel ID'

    if not channel_id:
        print(f"No channel found for handle: {handle}")
        exit()

    # Get channel info
    channel_info = get_channel_info(channel_id)
    channel_info["Channel ID"] = channel_id
    print(channel_info['Channel Name'], "done")
    upsert_channels_csv([channel_info], file_name=args.export_file)
    
elif int(one_or_multi) == 2:
    results = []

    for handle in handles:
        channel_id = get_channel_id(handle)

        if not channel_id:
            print(f"No channel found for handle: {handle}")
            continue

        # Get channel info
        channel_info = get_channel_info(channel_id)
        channel_info["Channel ID"] = channel_id
        print(channel_info['Sub Count'])

        results.append(channel_info)

    if results:
        make_channels_csv(results)
        upsert_channels_csv(results, file_name=args.export_file)
    else:
        print("No channel data to write.")
