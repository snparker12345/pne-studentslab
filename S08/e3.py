

import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8081
IP = "192.168.124.179" # it depends on the machine the server is running


while True:
    message = input("enter your message: ")

# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

# Send data. No strings can be sent, only bytes
# It necesary to encode the string into bytes
    s.send(message.encode())

    response = s.recv(1024)
    print("Response from server:", response.decode())
# Close the socket
    s.close()