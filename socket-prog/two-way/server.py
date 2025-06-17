import socket
import threading


# Continuously receive messages from the client
def recv(c):
    while True:
        m = c.recv(1024)
        if not m:
            break
        print("\r\033[KCLIENT:", m.decode())
        print("YOU ('exit' to exit): ", end="", flush=True)


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 12345))
s.listen(1)
c, a = s.accept()
print(f"\nConnected to {a}")
# Start a thread to handle incoming messages from the client non blockingly
threading.Thread(target=recv, args=(c,), daemon=True).start()

# Continuously send messages to the client
while True:
    m = input("YOU ('exit' to exit): ")
    if m == "exit":
        break
    c.sendall(m.encode())

# Close the connection and socket
s.close()
c.close()
