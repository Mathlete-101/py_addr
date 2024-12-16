import socket

# Replace with the server's IP address and port to connect to
host = 'localhost'  # Change this to the server's IP if not running locally
port = 33309

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))
    # Request the last stored IP address
    client_socket.sendall(b'REQUEST_IP')
    # Receive the IP address from the server
    data = client_socket.recv(1024)
    print(f'Received IP from server: {data.decode()}')
