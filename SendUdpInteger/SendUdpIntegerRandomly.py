import socket
import struct
import time
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 404
time_min_to_push=0.5
time_max_to_push=2.0
integer_min_range=-100
integer_max_range=100


#####################################
# Define the target IP and port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def push_integer(integer_value):
    packed_data = struct.pack('<i', integer_value)
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))
    print(f"Sent integer {integer_value} to {UDP_IP}:{UDP_PORT}")

if __name__ == "__main__":
    while True:
       time.sleep(time_min_to_push+ random.random()*(time_max_to_push-time_min_to_push) )
       push_integer(random.randint(integer_min_range,integer_max_range))

