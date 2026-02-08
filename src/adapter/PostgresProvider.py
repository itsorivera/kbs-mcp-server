from src.core.ports.KnowledgeBaseProvider import KnowledgeBaseProvider
from src.core.domain.models import KnowledgeBase
from typing import List

class PostgresKnowledgeBaseProvider(KnowledgeBaseProvider):
    @property
    def provider_type(self) -> str:
        return "postgres"

    async def list_knowledge_bases(self) -> List[KnowledgeBase]:
        return [
            KnowledgeBase(
                id="postgres-kb-1",
                name="Postgres_KB1",
                provider="postgres",
                description="Dummy Postgres KB 1"
            ),
            KnowledgeBase(
                id="postgres-kb-2",
                name="Postgres_KB2",
                provider="postgres",
                description="Dummy Postgres KB 2"
            )
        ]

    async def query_knowledge_bases(self, query: str) -> str:
        return "Postgres Result for query: " + query