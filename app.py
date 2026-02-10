from mcp.server.fastmcp import FastMCP
from typing import List
from src.config.AppConfig import discovery_service


mcp = FastMCP(
    name="kbs-mcp-server",
    instructions="""
    The KBS MCP Server is a server that provides tools to access different knowledge sources.

    ## Usage Workflow:
    1. ALWAYS start by using the list_knowledge_bases tool to discover available knowledge bases and their data sources
    2. Use the QueryKnowledgeBases tool to search specific knowledge bases with your natural language queries
    3. You can make multiple calls to QueryKnowledgeBases with different queries or targeting different knowledge bases
    """,
)

@mcp.tool(name="list_knowledge_bases")
async def list_knowledge_bases(provider_filter: str = None) -> List[dict]:
    """
    List all available knowledge bases.
    
    Args:
        provider_filter (str, optional): Filter by provider (e.g., 'amazon', 'postgres'). Defaults to None (all).
    """
    kbs = await discovery_service.list_knowledge_bases(provider_filter)
    # Convert dataclasses to dicts for JSON serialization
    return [kb.__dict__ for kb in kbs]



if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )