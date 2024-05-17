import asyncio
import websockets
import struct

async def echo(websocket, path):
    while True:
        async for message in websocket:
            # Unpack the byte array
            data = struct.unpack('<iiQ', message)
            int1, int2, ulong = data
            print(f"Received integers: {int1}, {int2} and unsigned long: {ulong}")
            

            # Echo the message back
            await websocket.send(message)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())


