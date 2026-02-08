from mcp.server.fastmcp import FastMCP, Context
import asyncio
from typing import List

from src.adapter.AmazonKnowledgeBaseProvider import AmazonKnowledgeBaseProvider
from src.adapter.PostgresProvider import PostgresKnowledgeBaseProvider

mcp = FastMCP(
    name="kbs-mcp-server",
    instructions="""
    The KBS MCP Server is a server that provides tools to access different knowledge sources.

    ## Usage Workflow:
    1. ALWAYS start by using the ListKnowledgeBases tool to discover available knowledge bases and their data sources
    2. Use the QueryKnowledgeBases tool to search specific knowledge bases with your natural language queries
    3. You can make multiple calls to QueryKnowledgeBases with different queries or targeting different knowledge bases
    """,
)

@mcp.tool()
async def get_weather(city: str, ctx: Context) -> str:
    """Get the weather for a city."""
    await ctx.info(f"Searched weather for {city}.")
    await ctx.report_progress(50, 100)
    await asyncio.sleep(2)
    await ctx.info(f"Found weather for {city}.")
    await ctx.report_progress(100, 100)
    return f"The weather in {city} is sunny."

@mcp.tool(name="ListKnowledgeBases")
async def list_knowledge_bases() -> List[str]:
    """List all avaibable knowledge bases."""


if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )