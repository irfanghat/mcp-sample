import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


async def main():
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langchain.agents import create_agent

    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_agent("openai:gpt-4.1", tools)
    response = await agent.ainvoke({"messages": "what is 3 + 9?"})

    print(response)


if __name__ == "__main__":
    asyncio.run(main())