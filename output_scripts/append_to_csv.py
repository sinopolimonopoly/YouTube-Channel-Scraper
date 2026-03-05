import csv
import os
    
def append_video_to_csv(row_dict, file_path):
    video_fields = [
        "Video ID",
        "Title",
        "Upload Date",
        "Numeric Date",
        "Video Type",
        "Duration",
        "Duration in s",
        "View Count",
        "Like Count",
        "Comment Count",
    ]

    with open(file_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=video_fields)
        writer.writerow(row_dict)