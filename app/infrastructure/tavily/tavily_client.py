# app/infrastructure/tavily/tavily_client.py

import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

class TavilyClientApi:
    def __init__(self):
        self.api_key = os.environ.get("TAVILY_SECRET_KEY")
        if not self.api_key:
            raise ValueError("TAVILY_SECRET_KEY environment variable is required.")
        self.tavily_client = TavilyClient(api_key=self.api_key)

    def get_info_company(self, prompt: str, max_results: int = 3) -> list:
        try:
            response = self.tavily_client.search(query=prompt, max_results=max_results, search_depth="advanced")
            return response.get('results', [])
        except Exception as e:
            raise RuntimeError(f"Error during Tavily API call: {str(e)}")
