from fastmcp.client import Client
import asyncio

async def demo():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[t.name for t in tools]}")
        
        # Add two numbers
        result = await client.call_tool(
            "add",
            {
                "a": 3,
                "b": 6
            }
        )
        print(f"Add result: {result.data}")

if __name__ == "__main__":
    asyncio.run(demo())