import socket
import time

# Receiver's IP address and Port (must match the receiver)
RECEIVER_IP = "127.0.0.1"
RECEIVER_PORT = 12345

# 1. Create a UDP socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print(f"UDP Sender sending to {RECEIVER_IP}:{RECEIVER_PORT}")

messages = ["Hello UDP!", "This is a test message.", "One more for good measure."]

try:
    for msg in messages:
        # Encode the string to bytes before sending
        data_to_send = msg.encode()

        # 2. Send data to the receiver's address
        sender_socket.sendto(data_to_send, (RECEIVER_IP, RECEIVER_PORT))
        print(f"Sent: '{msg}'")
        time.sleep(1)  # Wait a bit before sending next message

except KeyboardInterrupt:
    print("\nSender interrupted.")
finally:
    sender_socket.close()
