import socket
import threading


# Continuously receive messages from the server
def recv(s):
    while True:
        msg = s.recv(1024)
        if not msg:
            break
        print("SERVER:", msg.decode())


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(("127.0.0.1", 12345))
# start a thread to receive messages from the server non blockingly
threading.Thread(target=recv, args=(s,), daemon=True).start()

# Continuously send messages to the server
while True:
    m = input("Enter msg ('exit' to exit): ")
    if m == "exit":
        break
    s.sendall(m.encode())
s.close()
