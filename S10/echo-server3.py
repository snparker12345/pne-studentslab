import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# Initialize connection counter
connection_count = 0

# List to store client information
clients = []

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        connection_count += 1
        print(f"Connection {connection_count} from: {client_ip_port}")

        # Append client IP and port to the list
        clients.append(client_ip_port)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received from {client_ip_port}: {msg}")

        # -- Prepare the echo response
        echo_response = "ECHO: " + msg

        # -- The message has to be encoded into bytes
        cs.send(echo_response.encode())

        # -- Close the data socket
        cs.close()

    # Check if five clients have connected
    if connection_count >= 5:
        print("\nInformation of all clients:")
        for i, client in enumerate(clients, 1):
            print(f"Client {i}: {client}")
        break
