import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run() -> None:
    params = StdioServerParameters(command="python", args=["/workspace/mcp_demo/server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])
            result = await session.call_tool("echo", {"message": "hello mcp"})
            print("echo result:", result)


if __name__ == "__main__":
    asyncio.run(run())

