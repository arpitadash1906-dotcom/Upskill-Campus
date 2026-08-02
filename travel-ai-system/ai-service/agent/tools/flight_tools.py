print("flight_tools loaded successfully")  # 👈 HERE

from agent.tools.mcp_client import MCPClient

client = MCPClient("http://localhost:8001")

async def get_flights(source: str, destination: str):
    return await client.call_tool(
        "search_flights",
        {
            "source": source,
            "destination": destination
        }
    )