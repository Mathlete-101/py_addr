import socket
import os

# Replace with your listening IP address and port
host = '0.0.0.0'  # Listen on all interfaces
port = 33309

# Define the file path to save the IP address
file_path = os.path.join(os.path.expanduser('~'), 'received_ip.txt')

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f'Connected by {addr}')
            data = conn.recv(1024)
            if not data:
                break
            if data == b'REQUEST_IP':
                # Send the stored IP address back to the client
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        stored_ip = file.read().strip()
                    conn.sendall(stored_ip.encode('utf-8'))
                else:
                    conn.sendall(b'No IP stored')
            else:
                ip_address = data.decode()
                print(f'Received IP: {ip_address}')
                # Store the received IP address in a file
                with open(file_path, 'w') as file:
                    file.write(ip_address)
                # Send a success response back to the sender
                conn.sendall(b'success')
