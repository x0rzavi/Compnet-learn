import socket


def start_server(host="127.0.0.1", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one connection at a time
    print(f"Server started on {host}:{port}, waiting for a connection...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data or data.lower() == "exit":
                    print(f"Connection with {client_address} closed.")
                    break

                print(f"Client: {data}")
                server_response = input("You: ")
                client_socket.send(server_response.encode())

                if server_response.lower() == "exit":
                    print("Server is shutting down the connection.")
                    break
        except ConnectionResetError:
            print(f"Client {client_address} disconnected abruptly.")
        finally:
            client_socket.close()


if __name__ == "__main__":
    start_server()
