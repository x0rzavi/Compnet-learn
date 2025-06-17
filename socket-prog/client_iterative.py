import socket


def start_client(server_host="127.0.0.1", server_port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(
        f"Connected to server at {server_host}:{server_port}. Type 'exit' to disconnect."
    )

    try:
        while True:
            client_message = input("You: ")
            client_socket.send(client_message.encode())

            if client_message.lower() == "exit":
                print("You have disconnected from the server.")
                break

            server_response = client_socket.recv(1024).decode()
            if not server_response or server_response.lower() == "exit":
                print("Server disconnected.")
                break

            print(f"Server: {server_response}")
    except ConnectionResetError:
        print("Server disconnected abruptly.")
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()
