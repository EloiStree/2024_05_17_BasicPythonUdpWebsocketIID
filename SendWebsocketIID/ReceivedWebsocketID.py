import asyncio
import websockets
import struct

# pip3 install websockets
# pip3 install asyncio

debug_received_data = False


def handle_integer_received(integer):
    print(f"Received integer: {integer}")
    #Ajouter votre code ici
    print("Ajouter votre code ici")



################### Websocket don't touch  #####################


async def handle_message(websocket, path):
    async for message in websocket:
        message_length = len(message)
        
        if message_length == 4:
            value1 = struct.unpack('<i', message)[0]
            if debug_received_data:
                print(f"Received value: {value1} (format: <i)")
            handle_integer_received(int(value1))
        elif message_length == 12:
            value1, value2 = struct.unpack('<iQ', message)
            if debug_received_data:
                print(f"Received values: {value1}, {value2} (format: <iQ)")
            handle_integer_received(int(value1))
        
        elif message_length == 16:
            value1, value2, value3 = struct.unpack('<iiQ', message)
            if debug_received_data:
                print(f"Received values: {value1}, {value2}, {value3} (format: <iiQ)")
            handle_integer_received(int(value1))
        
        

start_server = websockets.serve(handle_message, "localhost", 7073)



asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server is listening on port 7073")
asyncio.get_event_loop().run_forever()
