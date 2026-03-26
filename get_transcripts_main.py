import sys
sys.stdout.reconfigure(encoding='utf-8')

import csv
import os
import time

from api_scripts.transcript_scripts.transcript_getter import get_transcript

channel = "curtisdoingthings"
output_folder = "transcript_output"
file_name = channel + "_transcripts.csv"
file_path = os.path.join(output_folder, file_name)

# Load existing transcripts so we don't re-fetch (avoids IP bans)
existing = {}  # video_id -> (title, transcript)
if os.path.exists(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vid = row.get("Video Id", "").strip()
            if vid and row.get("Transcript", "").strip():
                existing[vid] = (row.get("Title", ""), row.get("Transcript", ""))
    print(f"Loaded {len(existing)} existing transcripts from {file_path}")

# Collect (video_id, title) from your video list
input_rows = []
with open("output/curtisdoingthings_all_uploads_list.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        input_rows.append((row["Video ID"], row["Title"]))

# Build results: reuse existing transcript when present, else fetch
results = []
for video_id, title in input_rows:
    if video_id in existing:
        _, transcript = existing[video_id]
        results.append((video_id, title, transcript))
        print(f"{title[0:30]} - using existing transcript")
    else:
        transcript = get_transcript(video_id)
        results.append((video_id, title, transcript))
        print(f"{title[0:30]} - transcript retrieved")
        time.sleep(1.5)  # throttle requests to reduce IP ban risk

# Write all results (overwrites file so one source of truth)
os.makedirs(output_folder, exist_ok=True)
with open(file_path, 'w', newline='', encoding='utf-8') as transcript_csv:
    writer = csv.writer(transcript_csv)
    writer.writerow(["Video Id", "Title", "Transcript"])
    for video_id, title, transcript in results:
        writer.writerow([video_id, title, transcript])


#print(titles)

