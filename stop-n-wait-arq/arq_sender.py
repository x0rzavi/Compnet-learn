import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(2)  # 2 second timeout before thinking ACK lost
seq = 0

messages = ["Hello", "World", "Avishek"]

for msg in messages:
    while True:
        try:
            # Send message with sequence number
            s.sendto(f"{seq}|{msg}".encode(), ("127.0.0.1", 12345))
            print(f"Sending: {msg}")

            # Wait for ACK
            ack, _ = s.recvfrom(1024)
            ack_seq = int(ack.decode())

            if ack_seq != seq:  # Correct ACK received
                print(f"ACK received, message confirmed: {msg}")
                seq = 1 - seq  # Toggle sequence number
                break
        except socket.timeout:
            print(f"Timeout, retransmitting: {msg}")
    time.sleep(2)  # wait before sending another msg

s.close()
