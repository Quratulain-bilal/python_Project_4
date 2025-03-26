import socket
import threading

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 5555         # Port number
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # Allow up to 2 clients

clients = []

def handle_client(client):
    while True:
        try:
            # Receive data from one client
            data = client.recv(1024).decode('utf-8')
            if not data:
                break

            # Broadcast data to all other clients
            for c in clients:
                if c != client:
                    c.send(data.encode('utf-8'))
        except:
            break

    print("[DISCONNECTED]")
    clients.remove(client)
    client.close()

def start_server():
    print("[STARTING] Server is starting...")
    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start_server()