import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Server: {message}")

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    # Start a thread to listen for incoming messages
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            client.close()
            break
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()

# use this command in terminal to run the project;- python client.py
