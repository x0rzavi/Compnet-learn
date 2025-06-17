import socket

# AF_INET: IPv4 SOCK_STREAM: TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set socket options to allow reuse of the address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# For another server, you can use:
# s.connect(("0.tcp.in.ngrok.io", 15079))
s.connect(("127.0.0.1", 12345))

# Message sending loop
while True:
    m = input("Enter msg ('exit' to exit): ")
    if m == "exit":
        break
    # Send the message to the server
    s.sendall(m.encode("utf-8"))  # default is UTF-8 encoding
s.close()
