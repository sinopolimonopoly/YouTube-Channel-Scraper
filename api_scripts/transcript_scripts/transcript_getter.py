import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from youtube_transcript_api.proxies import WebshareProxyConfig, GenericProxyConfig

def get_transcript(video_id):

    try:
        # ytt_api = YouTubeTranscriptApi(
        #     proxy_config=GenericProxyConfig(
        #         http_url="http://vrbntaxn:xa7txihwky6d@154.203.43.247:5536",
        #         https_url="http://vrbntaxn:xa7txihwky6d@154.203.43.247:5536"
        #     )
        # )

        ytt_api = YouTubeTranscriptApi()

        raw_transcript = ytt_api.fetch(video_id)

        transcript = []
        trans_table = str.maketrans('', '', ".,")

        for snippet in raw_transcript.snippets:
            for word in snippet.text.split():
                word_no_punctuation = word.translate(trans_table)
                transcript.append(word_no_punctuation.lower())

        return " ".join(transcript)
    
    except TranscriptsDisabled: 
        print(f"!!!!!!Subtitles are disabled for video {video_id}!!!!!!")
        return "!X! SUBTITLES DISABLED !X!"

    except NoTranscriptFound: 
        print(f"!!!!!! No transcript found for video {video_id} !!!!!!")
        return "!X! NO TRANSCRIPT AVAIALABLE !X!"


    except Exception as e:
        print(f"!!! Unknown error while fetching transcript for video {video_id}")
        print(f"Error: {e}")
        return "UNKNOWN ERROR"

    except:
        print("How did we get here")
        return []