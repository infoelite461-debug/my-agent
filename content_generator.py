import openai

class ContentGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_caption(self, video_metadata, transcript):
        prompt = (f"Generate an engaging social media caption based on the following video metadata and transcript:
        \n        Video Title: {video_metadata['title']}\n" 
                 f"Description: {video_metadata['description']}\n" 
                 f"Transcript: {transcript}\n")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def generate_hashtags(self, video_metadata):
        prompt = (f"Generate relevant hashtags for the following video metadata:
        \n        Video Title: {video_metadata['title']}\n" 
                 f"Description: {video_metadata['description']}\n")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].split() # Splitting the hashtags into a list

# Example usage:
# generator = ContentGenerator(api_key='your_openai_api_key')
# caption = generator.generate_caption(video_metadata, transcript)
# hashtags = generator.generate_hashtags(video_metadata)