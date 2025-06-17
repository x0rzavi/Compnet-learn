import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 12345))
s.listen()
# Block until a client connects
c, a = s.accept()
print(f"Connected to {a}")

# Message receiving loop
while True:
    # Receive a message from the client
    try:
        m = c.recv(1024).decode("utf-8")
        if not m:  # If no message is received, break the loop, client disconnected
            break
        print(f"Message: {m}")
    except Exception:
        break
c.close()
