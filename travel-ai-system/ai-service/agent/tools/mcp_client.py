import httpx

class MCPClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def call_tool(self, tool, payload):
        print(f"Calling MCP → {self.base_url}/tools/{tool} with {payload}")  # 👈 ADD THIS

        async with httpx.AsyncClient() as client:
            res = await client.post(
                f"{self.base_url}/tools/{tool}",
                json=payload
            )

            print("Response status:", res.status_code)  # 👈 ADD THIS
            print("Response data:", res.text)           # 👈 ADD THIS

            return res.json()