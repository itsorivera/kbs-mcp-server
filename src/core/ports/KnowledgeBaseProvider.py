from abc import ABC, abstractmethod
from typing import List

class KBProvider(ABC):
    @abstractmethod
    async def list_knowledge_bases(self) -> List[str]:
        pass

    @abstractmethod
    async def query_knowledge_bases(self, query: str) -> str:
        pass