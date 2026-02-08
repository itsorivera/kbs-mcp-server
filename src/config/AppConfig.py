from src.adapter.AmazonKnowledgeBaseProvider import AmazonKnowledgeBaseProvider
from src.adapter.PostgresProvider import PostgresKnowledgeBaseProvider
from src.core.services.DiscoveryService import DiscoveryService

# Initialize Logic
amazon_provider = AmazonKnowledgeBaseProvider()
postgres_provider = PostgresKnowledgeBaseProvider() # Dummy
discovery_service = DiscoveryService(providers=[amazon_provider, postgres_provider])
