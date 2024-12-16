import socket
import time
import os

# Replace with your domain name
with open("domain.txt", "r") as file:
    domain_name = file.read().strip()
port = 33309

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  # Connect to Google DNS
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

while True:
    ip_address = get_ip_address()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((domain_name, port))
            sock.sendall(ip_address.encode('utf-8'))
            response = sock.recv(1024)
            if response == b'success':  # Expecting a success message
                break
    except Exception as e:
        print(f'Connection failed: {e}')
    time.sleep(10)
