from src.domain.models import ValueExpression
from src.infrastructure.tavily_client import TavilyClientApi


class NewAnalyzer:
    def __init__(self, tavily_client: TavilyClientApi):
        self.tavily_client = tavily_client

    async def analyze(self, expression: ValueExpression) -> str:
        prompt = f'Finance situation and news about:"{expression.content}"'
        return await self.tavily_client.getInfoCompany(prompt)