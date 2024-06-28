import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:4513"
    uri = "ws://81.240.94.97:4513"
    async with websockets.connect(uri) as websocket:
        key = "exampleKey"
        value = "exampleValue"
        
        # Create key-value string
        message = f"{key}:{value}"
        print(f"Sending message: {message}")
        
        # Send the message
        await websocket.send(message)
        
        # Receive the echoed message
        response = await websocket.recv()
        print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.run(send_message())
