# Python TCP Client-Server Networking Example

This project demonstrates basic networking using Python's `socket` library. The example includes a **TCP client** that sends a message to a **TCP server**, which then echoes the message back to the client. It is designed to help understand how to establish client-server communication, handle messages, and use sockets in Python.

## Project Overview

### Scripts:

- **client.py**: A TCP client that connects to a server, sends a message, receives a response, and then closes the connection.
- **server.py**: A TCP server that listens for incoming client connections, echoes back the received message, and then closes the connection.

## Prerequisites

Before running the scripts, ensure that you have Python 3.x installed on your machine.

### Required Libraries

This project uses Python's built-in `socket` library, which does not need to be installed manually. No third-party libraries are required for these scripts.

---

## How It Works

The client-server communication works as follows:

1. **server.py** starts first, creating a TCP server that listens on a specific IP (`127.0.0.1`) and port (`12345`).
2. **client.py** connects to the server using the same IP and port.
3. The client sends a simple message to the server.
4. The server receives the message and sends the same message back to the client.
5. The client receives the response and prints it to the console.
6. Both the client and the server close their connections.

---

## How to Run the Scripts

### 1. Run the Server Script (`server.py`)

The server script listens for incoming connections from clients on the specified IP and port.

To start the server, open a terminal and run:

```bash
python server.py
```

This will start the server and it will begin listening on `127.0.0.1:12345`.

### 2. Run the Client Script (`client.py`)

Once the server is running, the client script can be executed. Open another terminal window and run:

```bash
python client.py
```

This will establish a connection to the server, send a message, and wait for the response. Once the response is received, it will be printed to the console.

### 3. Communication Flow

- The server accepts incoming connections and listens for messages.
- When a connection is accepted, the server receives the message and sends the same message back (echoing it).
- The client receives the message from the server and prints it to the terminal.

---

## Script Details

### 1. **client.py** - TCP Client

This script is a simple TCP client that connects to the server, sends a message, waits for a response, and prints it.

#### Code Breakdown:

```python
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = '127.0.0.1'  # Localhost
port = 12345  # Server port

# Connect to the server
client_socket.connect((host, port))

# Send a message to the server
message = "Hello server, this is from the client"
client_socket.send(message.encode('utf-8'))

# Receive data from the server
data = client_socket.recv(1024).decode('utf-8')
print(f'Received from server: {data}')

# Close the socket
client_socket.close()
```

- **socket.socket(socket.AF_INET, socket.SOCK_STREAM)**: This creates a TCP socket that uses IPv4.
- **client_socket.connect((host, port))**: Connects to the server at `127.0.0.1` (localhost) and port `12345`.
- **client_socket.send(message.encode('utf-8'))**: Sends a message to the server, encoding it into bytes.
- **client_socket.recv(1024).decode('utf-8')**: Receives up to 1024 bytes from the server and decodes it back to a string.
- **client_socket.close()**: Closes the socket after communication is complete.

---

### 2. **server.py** - TCP Server

This script is a TCP server that listens for incoming client connections and echoes the received messages back.

#### Code Breakdown:

```python
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = '127.0.0.1'  # Localhost
port = 12345  # Port to listen on

# Bind the socket to the address
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5)

print(f'Server listening on {host}:{port}...')

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f'Connection established with {client_address}')

# Receive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f'Received: {data}')

# Echo the received data back to the client
client_socket.send(data.encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
```

- **socket.socket(socket.AF_INET, socket.SOCK_STREAM)**: Creates a TCP socket.
- **server_socket.bind((host, port))**: Binds the server to `127.0.0.1:12345` so it can listen for connections.
- **server_socket.listen(5)**: The server listens for up to 5 incoming connections.
- **client_socket, client_address = server_socket.accept()**: Accepts an incoming connection from the client and establishes a new socket for communication.
- **client_socket.recv(1024).decode('utf-8')**: Receives the data sent by the client.
- **client_socket.send(data.encode('utf-8'))**: Sends the same data back to the client (echo server).
- **client_socket.close()**: Closes the client connection.
- **server_socket.close()**: Closes the server socket.

---

## Notes

- **Firewall or Port Blocking**: Ensure that the port (`12345`) is not blocked by a firewall or in use by another service. If needed, choose a different port.
- **Simultaneous Runs**: Make sure to start the server before running the client, as the client needs to connect to a server that is already listening.
