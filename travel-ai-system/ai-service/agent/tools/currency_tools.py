from agent.tools.mcp_client import MCPClient

client = MCPClient("http://localhost:8004")

async def convert_currency(amount, from_c, to_c):
    return await client.call_tool("convert_currency", {
        "amount": amount,
        "from": from_c,
        "to": to_c
    })