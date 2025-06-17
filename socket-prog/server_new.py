import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\nClient: {message}\nYou: ", end="")
        except:
            print("\nClient disconnected.")
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(1)
    
    print("Server is waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Client {client_address} connected.")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        try:
            message = input("You: ")
            client_socket.send(message.encode())
        except:
            print("\nConnection closed.")
            break

    client_socket.close()
    server_socket.close()

start_server()
