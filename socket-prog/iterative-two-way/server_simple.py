import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 12345))
s.listen(2)

while True:
    c, a = s.accept()
    print(f"\nConnected to {a}")

    try:
        while True:
            # Receive from client first
            m = c.recv(1024)
            if not m:
                break
            print("CLIENT: ", m.decode())

            # Send reply to client
            reply = input("YOU ('exit' to disconnect): ")
            if reply == "exit":
                break
            c.sendall(reply.encode())
    except Exception:
        pass

    c.close()
    print(f"\nDisconnected from {a}")
