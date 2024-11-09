# app\infrastructure\open_ai\openai_client.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    def __init__(self):
        self.api_key = os.environ.get("SECRET_KEY_OPENAI")
        if not self.api_key:
            raise ValueError("SECRET_KEY_OPENAI environment variable is required.")
        openai.api_key = self.api_key

    def get_sentiment(self, prompt: str) -> str:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            # Log or handle specific exceptions as needed.
            raise RuntimeError(f"Error during OpenAI API call: {str(e)}")