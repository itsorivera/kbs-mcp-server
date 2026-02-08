from src.core.ports.KnowledgeBaseProvider import KnowledgeBaseProvider
from typing import List

class AmazonKnowledgeBaseProvider(KnowledgeBaseProvider):
    async def list_knowledge_bases(self) -> List[str]:
        return ["Amazon_KB1", "Amazon_KB2", "Amazon_KB3"]

    async def query_knowledge_bases(self, query: str) -> str:
        return "Amazon Result for query: " + query