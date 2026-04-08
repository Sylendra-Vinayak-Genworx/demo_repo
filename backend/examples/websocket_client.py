import asyncio

import websockets


async def main() -> None:
    uri = "ws://localhost:8000/ws/"

    async with websockets.connect(uri) as websocket:
        await websocket.send("hello world")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
