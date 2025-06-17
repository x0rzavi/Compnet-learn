import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\nServer: {message}\nYou: ", end="")
        except:
            print("\nServer disconnected.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        try:
            message = input("You: ")
            client_socket.send(message.encode())
        except:
            print("\nConnection closed.")
            break

    client_socket.close()

start_client()
