import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to connect to
host = '127.0.0.1'
port = 12345
  
#connecting to the server
client_socket.connect((host, port))

#send a message to the server
message = "Hello server, this is from the client"
client_socket.send(message.encode('utf-8'))

# Recieve data from the server
data = client_socket.recv(1024).decode('utf-8')
print(f'Received from server: {data}')

# Close the socket
client_socket.close()