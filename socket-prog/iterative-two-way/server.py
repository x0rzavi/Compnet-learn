import socket
import threading


# Continuously receive messages from the client
def recv(c, de):
    while True:
        try:
            m = c.recv(1024)
            if not m:
                de.set()  # Signal to stop the loop
                break
            print("\r\033[KCLIENT:", m.decode())
            print("YOU ('exit' to disconnect): ", end="", flush=True)
        except Exception:
            de.set()  # Signal to stop the loop
            break


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 12345))
s.listen(2)  # at most 2 connections can be queued

# Accept connections in a loop to handle multiple clients one by one, sequentially
while True:
    c, a = s.accept()
    print(f"\nConnected to {a}")

    # Create an event to signal when to disconnect
    de = threading.Event()

    # Start a new thread to handle receiving messages from the client non blockingly
    threading.Thread(target=recv, args=(c, de), daemon=True).start()

    # Continuously send messages to the current client
    while not de.is_set():
        try:
            m = input("YOU ('exit' to disconnect): ")
            if m == "exit":
                break
            c.sendall(m.encode())
        except Exception:
            break
    # Close the client connection when done with one client
    c.close()
    print(f"\nDisconnected from {a}")
