import boto3
from typing import List
from src.core.ports.KnowledgeBaseProvider import KnowledgeBaseProvider
from src.core.domain.models import KnowledgeBase
import logging
import os

logger = logging.getLogger(__name__)

class AmazonKnowledgeBaseProvider(KnowledgeBaseProvider):
    def __init__(self, region_name: str = "us-east-1"):
        # Allow region to be set via env var or default
        self.region_name = os.getenv("AWS_DEFAULT_REGION", region_name)
        self.client = boto3.client("bedrock-agent", region_name=self.region_name)
        self.tag_key = 'mcp-multirag-kb'

    @property
    def provider_type(self) -> str:
        return "amazon"

    async def list_knowledge_bases(self) -> List[KnowledgeBase]:
        logger.info(f"Listing Amazon Knowledge Bases in region {self.region_name}...")
        results = []
        paginator = self.client.get_paginator("list_knowledge_bases")
        
        try:
            for page in paginator.paginate():
                for kb_summary in page.get("knowledgeBaseSummaries", []):
                    kb_id = kb_summary.get("knowledgeBaseId")
                    name = kb_summary.get("name")
                    description = kb_summary.get("description", "")
                    
                    # Get details to check ARNs/Tags if strict filtering is needed
                    # Using the logic from discovery_amazon_kbs.py: check tags
                    
                    # We need the ARN to check tags
                    kb_details = self.client.get_knowledge_base(knowledgeBaseId=kb_id)
                    kb_arn = kb_details.get("knowledgeBase", {}).get("knowledgeBaseArn")
                    
                    if not kb_arn:
                        continue
                        
                    tags_response = self.client.list_tags_for_resource(resourceArn=kb_arn)
                    tags = tags_response.get("tags", {})
                    
                    if self.tag_key in tags and tags[self.tag_key] == 'true':
                        logger.debug(f"Found matching KB: {name} ({kb_id})")
                        
                        # Fetch data sources if needed, but for now just returning KB info
                        # The original script fetched data sources. 
                        # I'll modify the model to include data sources if possible, 
                        # but KnowledgeBase model has data_sources: List[Dict]
                        
                        data_sources = self._get_data_sources(kb_id)
                        
                        kb = KnowledgeBase(
                            id=kb_id,
                            name=name,
                            provider="amazon",
                            description=description,
                            data_sources=data_sources
                        )
                        results.append(kb)
        except Exception as e:
            logger.error(f"Error listing Amazon KBs: {e}")
            # Depending on requirements, we might want to re-raise or return empty
            # For now return what we have (or empty) to avoid crashing the whole discovery
            pass
            
        return results

    def _get_data_sources(self, kb_id: str) -> List[dict]:
        data_sources = []
        paginator = self.client.get_paginator("list_data_sources")
        try:
            for page in paginator.paginate(knowledgeBaseId=kb_id):
                for ds in page.get("dataSourceSummaries", []):
                    data_sources.append({
                        "id": ds.get("dataSourceId"),
                        "name": ds.get("name")
                    })
        except Exception as e:
            logger.error(f"Error listing data sources for KB {kb_id}: {e}")
        return data_sources

    async def query_knowledge_bases(self, query: str) -> str:
        # Placeholder for query logic
        return f"Amazon query result [Placeholder]: {query}"