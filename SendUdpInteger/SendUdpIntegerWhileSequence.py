import socket
import struct
import time
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 7072
time_before_start=3
time_between_push=1


sequence_integer=[
    101,
    201,
    102,
    202,
    103,
    203,
    104,
    204,
    105,
    205,
    106,
    206,
    107,
    207,
    108,
    208,
    109,
    209,
    110,
    210,
    111,
    211,
    112,
    212,
]

#####################################
# Define the target IP and port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def push_integer(integer_value):
    packed_data = struct.pack('<i', integer_value)
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))
    print(f"Sent integer {integer_value} to {UDP_IP}:{UDP_PORT}")

if __name__ == "__main__":
    while True:
        time.sleep(time_before_start)
        for integer in sequence_integer:
            push_integer(integer)
            time.sleep(time_between_push)


