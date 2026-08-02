print("places_tools loaded successfully")  # debug

from agent.tools.mcp_client import MCPClient

client = MCPClient("http://localhost:8003")

async def get_places(city: str):
    return await client.call_tool("search_places", {
        "city": city
    })