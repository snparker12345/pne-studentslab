from Client0 import Client


IP = "212.128.255.66" # your IP address
PORT = 8080
c = Client(IP, PORT)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
