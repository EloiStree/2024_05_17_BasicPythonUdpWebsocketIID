import socket

def udp_receiver():
    listen_ip = "0.0.0.0"  # Listen on all available interfaces
    listen_port = 12345    # Port number to listen on

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP and port
    sock.bind((listen_ip, listen_port))

    print(f"Listening for messages on {listen_ip}:{listen_port}")

    while True:
        # Receive message
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message from {addr}: {data.decode()}")

if __name__ == "__main__":
    udp_receiver()
