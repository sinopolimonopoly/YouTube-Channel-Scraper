# Youtube Channel Video Scraper

## What this is
A series of Python scripts to fetch a list of a YouTube Channel's long form videos, shorts and livestreams, along with their upload date, durations, view, like and comment counts. 

## How it's done
Uses a YouTube Data V3 API key created with Google Cloud Console project.  
The API key is used to make requests and fetch json results, which are then parsed with Python to retrieve and structure the desired information.

### Steps
1. Specify the handle of the YouTube channel
2. Specify the desired type of videos: Long form (regular videos), Short, Livestream, or all
3. Retrieve the channel ID of the handle
4. Retrieve the playlist ID of the channel's uploaded videos and/or shorts
5. Fetch the video ID of all the videos in the playlist(s)
6. Fetch information for each video using its ID
7. Convert the created Python dictionary to a csv file

## Retrieved Fields
|Field       |Type      |Example     |
|------------|----------|------|
|Video ID  |String    | CACAmH4r1fw |
|Title | String | Bowling Trick Shots \| Dude Perfect |
|Upload Date |  String | 	2014-06-02 |
|Video Type | Categorical | Long Form	|
|Duration | String | 6M1S	|
|Duration in s| Int | 361 |
|View count| Int | 101744166 |	
|Like Count | Int | 681701 |
|Comment Count | Int | 44255 |

* Note that likes and comments may be disabled on a video. In this case, the fields will contain "Disabled" instead of an integer.
* Note that currently ongoing livestreams will not have an integer duration.


## Final Data Structure
Dictionary of dictionaries  
{"Video ID 1": {"Title": str, "Upload Date": str, "Video Type": categorical, "Duration": str, "Duration in s": int, "View Count": int, "Like Count": int, "Comment Count": int}, "Video ID 2": {...}, ...}  

## How to Use
1. Clone this repo
2. Create a new project on console.cloud.google.com
3. In APIs & Services, find YouTube Data API V3 and create credentials for it
4. Choose public data and create your API key
5. In the cloned repo, create a file ".env" on the same level as the README
6. Set API_KEY = "your API key" in the .env file
7. Run the main.py file
8. Find and download the csv file created in the output scripts
