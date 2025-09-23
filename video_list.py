import sys
sys.stdout.reconfigure(encoding='utf-8')

import csv
import os

video_ids = []
titles = []

i = 0

with open("output/maxthemeatguy_shorts_list.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        video_id = row["Video ID"]
        video_ids.append(video_id)

        title = row["Title"]
        titles.append(title)


print("0th SEGMENT")
print(video_ids[0:50])
print(titles[0:50])
print("-------------------------------------------------\n")
print("\n")


print("1st SEGMENT")
print(video_ids[50:100])
print(titles[50:100])
print("-------------------------------------------------\n")
print("\n")

print("SECOND SEGMENT")
print(video_ids[100:200])
print(titles[100:200])
print("-------------------------------------------------\n")
print("\n")


print("THIRD SEGMENT")
print(video_ids[200:300])
print(titles[200:300])
print("-------------------------------------------------\n")
print("\n")


print("FOURTH SEGMENT")
print(video_ids[300:400])
print(titles[300:400])
print("-------------------------------------------------\n")
print("\n")

print("LAST SEGMENT")
print(video_ids[400:])
print(titles[400:])





