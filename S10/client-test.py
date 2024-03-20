
from Client0 import Client
import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8081
IP = "192.168.124.179" # it depends on the machine the server is running
client = Client(IP, PORT)

# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))


try:
        # Send messages
    for i in range(5):
        message = f"message {i}"
        client.talk(message)
        print(f"Sent: {message}")
except Exception as e:
    print("An error occurred:", e)
finally:
        # Close the connection
    s.close()


