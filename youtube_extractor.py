import requests
import json
from typing import Any, Dict, List

# Class for handling YouTube video data extraction
class YouTubeExtractor:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://www.googleapis.com/youtube/v3/'

    def get_video_metadata(self, video_id: str) -> Dict[str, Any]:
        url = f'{self.base_url}videos?part=snippet,contentDetails,statistics&id={video_id}&key={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve video metadata')

    def get_transcript(self, video_id: str) -> List[str]:
        # Assuming transcripts are publicly available
        url = f'https://video.google.com/timedtext?lang=en&v={video_id}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.split('\n')
        else:
            raise Exception('Failed to retrieve transcript')

    def gather_video_info(self, video_id: str) -> None:
        metadata = self.get_video_metadata(video_id)
        transcript = self.get_transcript(video_id)

        # Display gathered information
        print(json.dumps(metadata, indent=4))
        print(json.dumps(transcript, indent=4))

# Example Usage:
# extractor = YouTubeExtractor(api_key='YOUR_API_KEY')
# extractor.gather_video_info(video_id='VIDEO_ID')
