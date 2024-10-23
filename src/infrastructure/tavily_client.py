import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


class TavilyClientApi:
    def __init__(self):
        self.api_key = os.environ.get("TAVILY_SECRET_KEY")
        self.tavily_client = TavilyClient(api_key=self.api_key)

    async def getInfoCompany(self, prompt: str) -> str:
        response = self.tavily_client.search(query=prompt, max_results=1, search_depth="advanced")
        return response['results']