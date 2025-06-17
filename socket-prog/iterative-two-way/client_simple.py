import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))

try:
    while True:
        # Send message to server first
        m = input("YOU ('exit' to exit): ")
        if m == "exit":
            break
        s.sendall(m.encode())

        # Receive reply from server
        reply = s.recv(1024)
        if not reply:
            break
        print("SERVER: ", reply.decode())
except Exception:
    pass

s.close()
