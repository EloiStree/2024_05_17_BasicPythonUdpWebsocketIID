def handle_integer_received(integer):
    value = int(integer)
    print(value)


############################################################
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
            if len(data) == 4:
                # 4 bytes: Single integer
                received_integer = struct.unpack('<i', data)[0]
                handle_integer_received(received_integer)
            elif len(data) == 8:
                # 8 bytes: Two integers (index and value)
                index, value = struct.unpack('<ii', data)
                print(f"Received index: {index}, value: {value}")
            elif len(data) == 12:
                # 12 bytes: One integer and one unsigned long long (integer + Q)
                received_integer, large_value = struct.unpack('<iQ', data)
                print(f"Received integer: {received_integer}, large value: {large_value}")
            elif len(data) == 16:
                # 16 bytes: Two integers and one unsigned long long
                int1, int2, large_value = struct.unpack('<iiQ', data)
                print(f"Received integers: {int1}, {int2}, large value: {large_value}")
            else:
                print(f"Unexpected data length ({len(data)} bytes) received from {address}. Ignoring.")
                continue
            
    except KeyboardInterrupt:
        print("UDP integer listener client stopped.")
    finally:
        # Close the socket
        udp_socket.close()

# Example usage:
if __name__ == "__main__":
    HOST = "0.0.0.0"   # Listen on all available interfaces
    PORT = 404         # Example port (change to your desired port)
    integer_listener_client_udp(HOST, PORT)
