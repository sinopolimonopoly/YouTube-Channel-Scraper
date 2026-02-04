import csv
import os

from datetime import datetime

def make_channels_csv(channel_dict_list, output_folder="channel_output"):
        os.makedirs(output_folder, exist_ok=True)

        file_name = f"{channel_dict_list[0]['Channel Time']}_and_channels_info.csv"
    
        file_path = os.path.join(output_folder, file_name)

        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                # Create writer object
                writer = csv.writer(csv_file)
                # Create the header
                writer.writerow(["Handle", "Channel Name", "Join Date", "Description", "Thumbnail URL", "Subscriber Count", "View Count", "Video Count"])

                # For every video in the dictionary, grab the ID (key) and the corresponding dictionary (value) that holds all the information
                for channel_dict in channel_dict_list:
                    #########
                    # Variables for fields
                    handle = channel_dict['Handle']
                    channel_name = channel_dict['Channel Name']
                    join_date = channel_dict['Join Date']
                    description = channel_dict['Description']
                    thumbnail_url = channel_dict['Thumbnail URL']
                    sub_count = channel_dict['Sub Count']
                    view_count = channel_dict['View Count']
                    video_count = channel_dict['Video Count']


                    # Write new row with all the channel_dict_list
                    writer.writerow([handle, channel_name,join_date, description, thumbnail_url, sub_count, view_count, video_count])
