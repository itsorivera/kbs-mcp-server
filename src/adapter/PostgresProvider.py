from src.core.ports.KnowledgeBaseProvider import KnowledgeBaseProvider
from typing import List

class PostgresKnowledgeBaseProvider(KnowledgeBaseProvider):
    async def list_knowledge_bases(self) -> List[str]:
        return ["Postgres_KB1", "Postgres_KB2", "Postgres_KB3"]

    async def query_knowledge_bases(self, query: str) -> str:
        return "Postgres Result for query: " + query