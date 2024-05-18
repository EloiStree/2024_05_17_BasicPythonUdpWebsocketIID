import asyncio
import websockets
import random
import time
uri = "ws://localhost:7073"

min_int = -100
max_int = 100
min_sleep = 4
max_sleep = 10


async def send_random_integers(uri):
    async with websockets.connect(uri) as websocket:
        while True:

            random_integer = random.randint(min_int, max_int)
            integer_as_byte = random_integer.to_bytes(4, 'little', signed=True)
            await websocket.send(integer_as_byte)
            print(f"Sent: {random_integer}")
            
            await asyncio.sleep(random.uniform(min_sleep, max_sleep))

asyncio.get_event_loop().run_until_complete(send_random_integers(uri))
