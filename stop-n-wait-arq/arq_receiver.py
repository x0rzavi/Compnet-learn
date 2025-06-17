import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 12345))
seq = 0
ack_loss_prob = 0.3  # 30% ACK loss probability

while True:
    data, addr = s.recvfrom(1024)
    recv_seq = int(data.decode().split("|")[0])
    msg = data.decode().split("|")[1]

    if recv_seq == seq:  # expected packet received
        print(f"Received: {msg}")
        seq = 1 - seq  # Toggle between 0 and 1

    # Simulate ACK loss
    if random.random() > ack_loss_prob:
        s.sendto(str(seq).encode(), addr)
        print(f"ACK sent: {seq}")
    else:
        print("ACK lost simulated!")
