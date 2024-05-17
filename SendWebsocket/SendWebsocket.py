import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = "Hello, WebSocket!"
            print(f"Sending message: {message}")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Recoveryeived response: {response}")
            asyncio.sleep(1)

if __name__ == "__main__":
    
    asyncio.run(send_message())
