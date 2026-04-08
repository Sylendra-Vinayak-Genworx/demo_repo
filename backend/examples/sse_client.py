import asyncio

import httpx


async def main() -> None:
    url = "http://localhost:8000/events/"

    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            async for line in response.aiter_lines():
                if line:
                    print(line)


if __name__ == "__main__":
    asyncio.run(main())
