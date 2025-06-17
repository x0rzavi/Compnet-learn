import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 12345))
s.listen(2)  # up to 2 clients can be queued

# Accept connections in a loop to handle multiple clients sequentially, one by one
while True:
    c, a = s.accept()
    print(f"\nConnected to {a}")

    # Continuously receive messages from the client
    while True:
        try:
            m = c.recv(1024).decode()
            if not m:
                break
            print(f"Message: {m}")
        except Exception:
            break
    # Close the client connection when done with one client
    print(f"\nDisconnected from {a}")
    c.close()
