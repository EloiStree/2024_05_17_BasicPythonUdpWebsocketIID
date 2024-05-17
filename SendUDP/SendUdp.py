import socket
import time
def udp_sender():
    server_ip = "127.0.0.1"  # IP address of the receiver
    server_port = 12345      # Port number of the receiver
    message = "Hello, UDP!"

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send message
        print(f"Sending message to {server_ip}:{server_port}")
        sock.sendto(message.encode(), (server_ip, server_port))
        print("Message sent")
    finally:
        sock.close()

if __name__ == "__main__":
    while True:
        udp_sender()
        time.sleep(1)
