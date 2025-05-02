import csv
import os

# Function to create csv (excel) file for all the videos
def create_video_csv(video_dict, channel, video_type, output_folder="output"):

    # Make sure destination folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Create file name with channel handle
    file_name = f'{channel}_{'_'.join(video_type.split(" "))}_list.csv'

    # Add path so file knows where to go
    file_path = os.path.join(output_folder, file_name)

    # Specify file name and writing operation
    # newline='' prevents unnecessary line breaks between rows
    # utf-8 encoding ensures safe handling of emojis, international characters...
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        # Create writer object
        writer = csv.writer(csv_file)
        # Create the header
        writer.writerow(["Video ID", "Title", "Upload Date", "Video Type", "Duration", "Duration in s", "View Count", "Like Count", "Comment Count"])

        # For every video in the dictionary, grab the ID (key) and the corresponding dictionary (value) that holds all the information
        for video_id, info in video_dict.items():
            
            # Variables for fields
            title = info['Title']
            upload_date = info['Upload Date']
            video_type = info['Video Type']
            duration = info['Duration']
            duration_in_s = info['Duration in s']
            view_count = info['View Count']
            like_count = info['Like Count']
            comment_count = info['Comment Count']

            # Write new row with all the info
            writer.writerow([video_id, title, upload_date, video_type, duration, duration_in_s, view_count, like_count, comment_count])
