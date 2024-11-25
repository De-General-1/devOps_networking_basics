import socket

# Creating a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define the host and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the address
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5) 

print(f'Server listening on {host}:{port}...')

# Accept a connection and get the client socket
client_socket, client_address = server_socket.accept()
print(f'Connection established with {client_address}')
print(f'Connection established client socket of {client_address}')

# Receive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f'Received: {data}')

# Echo the received data back to the client
client_socket.send(data.encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()