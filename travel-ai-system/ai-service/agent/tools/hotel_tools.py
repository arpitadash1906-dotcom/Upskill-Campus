print("hotel_tools loaded successfully")  # debug

from agent.tools.mcp_client import MCPClient

client = MCPClient("http://localhost:8002")

async def get_hotels(city: str):
    return await client.call_tool("search_hotels", {
        "city": city
    })