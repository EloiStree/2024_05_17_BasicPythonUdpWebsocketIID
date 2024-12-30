

import socket
import time
import random

UDP_IP = "81.240.94.97"
UDP_IP = "helloworld42.ddns.net"
UDP_PORT = 3615

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = str(random.randint(0, 100)).encode('utf-8')
    sock.sendto(message, (UDP_IP, UDP_PORT))
    time.sleep(1)