from abc import ABC, abstractmethod
from typing import List
from src.core.domain.models import KnowledgeBase

class KnowledgeBaseProvider(ABC):
    @property
    @abstractmethod
    def provider_type(self) -> str:
        pass

    @abstractmethod
    async def list_knowledge_bases(self) -> List[KnowledgeBase]:
        pass

    @abstractmethod
    async def query_knowledge_bases(self, query: str) -> str:
        pass