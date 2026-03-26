import requests
import os

from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")

url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,snippet,statistics&id=lKj9JCrFGhk&key={api_key}"
url2 =f"https://www.googleapis.com/youtube/v3/videos?part=id,snippet,contentDetails,statistics,status,topicDetails,recordingDetails,liveStreamingDetails,player,localizations,paidProductPlacementDetails&key={api_key}&id=sWVKiBsdvRA"
url3 = f""
res = requests.get(url2)
data = res.json()
print(data)
