
from Client0 import Client
import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "212.128.254.253" # it depends on the machine the server is running
client = Client(IP, PORT)

try:
        # Send messages
    for i in range(5):
        message = f"message {i}"
        client.talk(message)
        print(f"Sent: {message}")
except Exception as e:
    print("An error occurred:", e)


