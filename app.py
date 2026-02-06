from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def get_weather(city: str):
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

def main():
    mcp.run()

if __name__ == "__main__":
    main()