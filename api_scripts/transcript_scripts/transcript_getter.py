import sys
sys.stdout.reconfigure(encoding='utf-8')

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()

    raw_transcript = ytt_api.fetch(video_id)
    print(raw_transcript)

    try:
        ytt_api = YouTubeTranscriptApi()

        raw_transcript = ytt_api.fetch(video_id)

        transcript = []
        trans_table = str.maketrans('', '', ".,")

        for snippet in raw_transcript.snippets:
            for word in snippet.text.split():
                word_no_punctuation = word.translate(trans_table)
                transcript.append(word_no_punctuation.lower())

        print(transcript)
        return " ".join(transcript)
    
    except:
        print("Youtube Transcript API Error")
        return []
    

print(get_transcript("muReNBeUz2Q"))


