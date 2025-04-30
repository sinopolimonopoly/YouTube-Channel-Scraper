import csv

def create_video_csv(video_dict):

    with open('video_list.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Video ID", "Title", "Upload Date", "Duration", "Duration in s", "View Count", "Like Count", "Comment Count"])

        for video_id, info in video_dict.items():
            
            title = info['Title']
            upload_date = info['Upload Date']
            duration = info['Duration']
            duration_in_s = info['Duration in s']
            view_count = info['View Count']
            like_count = info['Like Count']
            comment_count = info['Comment Count']

            writer.writerow([video_id, title, upload_date, duration, duration_in_s, view_count, like_count, comment_count])
