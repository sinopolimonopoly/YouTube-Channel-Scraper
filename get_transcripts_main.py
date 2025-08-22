import sys
sys.stdout.reconfigure(encoding='utf-8')

import csv
import os

from api_scripts.transcript_scripts.transcript_getter import get_transcript

video_ids = []
titles = []
transcripts = []

with open("output/curtisdoingthings_all_uploads_list.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        video_transcript = get_transcript(row["Video ID"])

        video_ids.append(row["Video ID"])
        titles.append(row["Title"])
        transcripts.append(video_transcript)

        print(row["Title"][0:30] + " - transcript retrieved")


channel = "curtisdoingthings"
file_name = channel + "_transcripts.csv"

output_folder = "transcript_output"

file_path = os.path.join(output_folder, file_name)

with open(file_path, 'w', newline='', encoding='utf-8') as transcript_csv:
    writer = csv.writer(transcript_csv)

    writer.writerow(["Video Id", "Title", "Transcript"])
    
    for idx in range(0,len(video_ids)):
        video_id = video_ids[idx]
        title = titles[idx]
        transcript = transcripts[idx]
        print([video_id, title, transcript])

        writer.writerow([video_id, title, transcript])


#print(titles)

