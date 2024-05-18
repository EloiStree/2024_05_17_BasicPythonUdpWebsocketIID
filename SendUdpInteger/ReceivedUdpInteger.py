def handle_integer_received(integer):
    value=int(integer)
    print(value)




import socket
import struct

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

# Example usage:
if __name__ == "__main__":
    HOST = "0.0.0.0"   # Listen on all available interfaces
    PORT = 404       # Example port (change to your desired port)
    integer_listener_client_udp(HOST, PORT)
