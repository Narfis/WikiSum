from openai import OpenAI
from  dotenv import load_dotenv
import os

class ChatGPT:
    def __init__(self):
        load_dotenv()
        self.cut_off = 8_000


        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def summarise_wikipedia_post(self, wiki_content):

        if len(wiki_content) > self.cut_off:
            wiki_content = wiki_content[:self.cut_off]

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant summarising wikipedia posts into an easy to read text."
                },
                {
                    "role": "user",
                    "content": wiki_content
                }
            ]
        )
        return completion
    
    def key_points(self, wiki_content):
        cut_off = 8_000
        if len(wiki_content) > cut_off:
            wiki_content = wiki_content[:cut_off]

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant adding the top 5 points from a wikipedia post into a bulletlist format."
                },
                {
                    "role": "user",
                    "content": wiki_content
                }
            ]
        )
        return completion
    
