# Source : https://github.com/EloiStree/2024_05_17_BasicPythonUdpWebsocketIID/tree/main/LocalWebsocketServerToBroadcast

websocket_server_port=7073
udp_server_port = 7072

# List of IP:PORT to broadcast the data to the apps    
broadcast_list_udp_target={"127.0.0.1:404"}

# Set to True if you want to print the received data of clients
debug_received_data = False

def handle_integer_received(integer):
    i=int(integer)
    # If you want it out of the script
    YourCodeHere.handle_integer_received(integer)
    # if you want to broadcast the data to apps with UDP
    broadcast_to_targets(int(i))
    ## If you want in the script
    print(f"R|{integer}")









################### Websocket don't touch  #####################

import asyncio
import websockets
import struct
import os
import socket

# pip3 install websockets
# pip3 install asyncio
# pip3 install struct
# pip3 install socket


filename = "YourCodeHere.py"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        # You can add initial content to the file if you want
        f.write("""# YourCodeHere.py
def handle_integer_received(integer):
    i=int(integer)""")
    print(f"File '{filename}' created successfully!")


import YourCodeHere

def broadcast_to_targets(message):
    for target in broadcast_list_udp_target:
        temp = target.split(":")
        target_address = ("127.0.0.1", "")

        if len(temp) == 2:
            target_address = (temp[0], int(temp[1]))  
        elif len(temp) == 1:
            target_address = ("", int(temp[0]))  

        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(struct.pack('<i', message), target_address)
        udp_socket.close()

def get_current_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


async def handle_message(websocket, path):
    try:
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
    except websockets.ConnectionClosedError as e:
            print(f"Connection closed with error: {e}")
            # Wait a bit before trying to reconnect
            await asyncio.sleep(5)
        
        
        

start_server = websockets.serve(handle_message, "", websocket_server_port)



asyncio.get_event_loop().run_until_complete(start_server)


print("Current IP:", get_current_ip())
print("WebSocket server is listening on port 7073")







################### UDP don't touch  #####################

def integer_listener_client_udp(host, port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the host and port
    udp_socket.bind((host, port))
    print("UDP integer listener client is now listening on {}:{}".format(host, port))

    try:
        while True:
            # Receive data from the socket
            data, address = udp_socket.recvfrom(64)
            if len(data)==4:
                received_integer = struct.unpack('<i', data)[0]
                handle_integer_received(received_integer)
            elif len(data)==12:
                received_integer = struct.unpack('<iQ', data)[0]
                handle_integer_received(received_integer)
            elif len(data)==16:
                received_integer = struct.unpack('<iiQ', data)[0]
                handle_integer_received(received_integer)
            else: continue
            #print("Received integer:", received_integer, "from", address)
            
    except KeyboardInterrupt:
        print("UDP integer listener client stopped.")
    finally:
        # Close the socket
        udp_socket.close()


    
asyncio.get_event_loop().run_in_executor(None, integer_listener_client_udp, "", udp_server_port)











asyncio.get_event_loop().run_forever()
