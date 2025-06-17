import socket
import threading


# This server accepts multiple clients and handles each client in a separate thread
def handle_client(c, a):
    print(f"Connected to {a}")
    # Continuously receive messages from the client
    while True:
        try:
            m = c.recv(1024).decode()
            if not m:
                break
            print(f"{a}: {m}")
        except Exception:
            break
    c.close()
    print(f"Client {a} disconnected")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 12345))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(2)  # up to 2 clients can be queued

# Accept connections in a loop to handle multiple clients concurrently
while True:
    c, a = s.accept()
    # Start a new thread to handle the client connection
    threading.Thread(target=handle_client, args=(c, a)).start()
