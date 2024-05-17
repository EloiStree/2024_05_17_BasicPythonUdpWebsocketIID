import asyncio
import websockets
import struct
import time

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            int1 = 12345
            int2 = 67890
            ulong = 12345678901234567890
        
            # Pack the data into a byte array
            message = struct.pack('<iiQ', int1, int2, ulong)
            print(f"Sending byte array: {message}")
        
            # Send the byte array
            await websocket.send(message)
        
            # Receive the echoed byte array
            response = await websocket.recv()
        
            # Unpack the response
            received_data = struct.unpack('<iiQ', response)
            received_int1, received_int2, received_ulong = received_data
            print(f"Received integers: {received_int1}, {received_int2} and unsigned long: {received_ulong}")
            
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(send_message())
