from typing import List, Optional, Dict
from src.core.domain.models import KnowledgeBase
from src.core.ports.KnowledgeBaseProvider import KnowledgeBaseProvider
import asyncio
import logging

logger = logging.getLogger(__name__)

class DiscoveryService:
    def __init__(self, providers: List[KnowledgeBaseProvider]):
        self.providers: Dict[str, KnowledgeBaseProvider] = {p.provider_type: p for p in providers}

    async def list_knowledge_bases(self, provider_filter: Optional[str] = None) -> List[KnowledgeBase]:
        logger.info(f"Listing KBs with filter: {provider_filter}")
        if provider_filter:
            if provider_filter in self.providers:
                try:
                    return await self.providers[provider_filter].list_knowledge_bases()
                except Exception as e:
                    logger.error(f"Error fetching KBs from {provider_filter}: {e}")
                    return []
            else:
                logger.warning(f"Provider {provider_filter} not found. Available: {list(self.providers.keys())}")
                return []
        
        # If no filter, aggregate all
        tasks = [p.list_knowledge_bases() for p in self.providers.values()]
        # asyncio.gather returns a list of results (each result is a List[KnowledgeBase])
        
        # Use return_exceptions=True to prevent one failure from stopping all
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        final_list = []
        for i, res in enumerate(results):
            if isinstance(res, Exception):
                provider_name = list(self.providers.keys())[i]
                logger.error(f"Error fetching KBs from {provider_name}: {res}")
            elif isinstance(res, list):
                final_list.extend(res)
        
        return final_list
