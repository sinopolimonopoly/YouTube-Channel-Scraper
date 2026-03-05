import csv
import os

def create_output_csv(handle, video_type, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)

    file_name = f"{handle}_{'_'.join(video_type.split(' '))}_list.csv"
    file_path = os.path.join(output_folder, file_name)

    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Video ID", "Title", "Upload Date", "Numeric Date", "Video Type", "Duration", "Duration in s", "View Count", "Like Count", "Comment Count"])

    return file_path