import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 404


def fetch_integer():
    user_input = input("Enter an integer: ")
    try:
        integer_value = int(user_input)
        push_integer(integer_value)
    except ValueError:
        ignore =  0
     

#####################################
# Define the target IP and port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def push_integer(integer_value):
    packed_data = struct.pack('<i', integer_value)
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))
    print(f"Sent integer {integer_value} to {UDP_IP}:{UDP_PORT}")

if __name__ == "__main__":
    while True:
       fetch_integer()
