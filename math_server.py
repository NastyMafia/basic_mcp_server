h# ... imports and tool definitions ...
import os
from fastmcp import FastMCP
from langchain_tavily import TavilySearch

from dotenv import load_dotenv
load_dotenv()

search_tool = TavilySearch(max_results=3)
mcp = FastMCP("Search")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def search(query: str) -> str:
    """
    Search the internet.
    """
    try:
        return str(search_tool.invoke(query))
    except Exception as e:
        return f"Search Error: {str(e)}"

if __name__ == "__main__":
    # Get the PORT from the cloud environment, default to 8000 if running locally
    port = int(os.environ.get("PORT", 8000))
    
    # IMPORTANT: host must be "0.0.0.0" to work in Docker/Cloud

    mcp.run(transport="sse", host="0.0.0.0", port=port)
