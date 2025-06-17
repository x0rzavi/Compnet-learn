import socket

# Receiver's IP address and Port
RECEIVER_IP = "127.0.0.1"
RECEIVER_PORT = 12345

# 1. Create a UDP socket
# AF_INET for IPv4, SOCK_DGRAM for UDP
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2. Bind the socket to the IP address and port
# This makes the receiver listen on this address and port
receiver_socket.bind((RECEIVER_IP, RECEIVER_PORT))
print(f"UDP Receiver listening on {RECEIVER_IP}:{RECEIVER_PORT}")

try:
    while True:
        # 3. Receive data
        # recvfrom returns (data, address_of_sender)
        # 1024 is the buffer size, maximum bytes to receive
        data, sender_address = receiver_socket.recvfrom(1024)

        # Decode the bytes to a string for printing
        message = data.decode()
        print(f"Received '{message}' from {sender_address}")

except KeyboardInterrupt:
    print("\nReceiver shutting down.")
finally:
    receiver_socket.close()
