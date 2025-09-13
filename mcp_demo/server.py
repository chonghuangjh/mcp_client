import asyncio
from typing import Any, Dict

from mcp.server import Server
from mcp.server.stdio import stdio_server


server = Server("demo-server")


@server.tool()
async def echo(message: str) -> Dict[str, Any]:
    return {"echo": message}


async def main() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write)


if __name__ == "__main__":
    asyncio.run(main())

