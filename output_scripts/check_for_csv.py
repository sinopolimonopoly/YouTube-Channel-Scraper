import csv
import os

def check_if_csv_exists(handle, video_type, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)

    file_name = f"{handle}_{'_'.join(video_type.split(' '))}_list.csv"
    file_path = os.path.join(output_folder, file_name)

    return os.path.isfile(file_path)