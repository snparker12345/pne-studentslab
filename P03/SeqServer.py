import socket
from Client0 import Client

from Seq0 import Seq

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

s1 = Seq()
s1.read_fasta("ADA.txt")
seq_list = ["ACT", "GATA", "CAGATA", "BCC"]


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
        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message
        msg = msg.strip()


        msg = msg.strip()
        response = ""
        splitted = msg.split()
        if msg.__eq__("PING"):
            response = "OK"
            print(f"{msg} command!")
            print("OK")
        elif splitted[0] == "GET":
            num = int(splitted[1])
            print("GET")
            print(seq_list[num])
        elif splitted[0] == "INFO":
            split = Seq(splitted[1])
            print(f"Sequence:{splitted[1]}")
            print(f"Length: {split.len()}")
            for base in "ATCG":
                print(f"{base}: {split.count_base(base)}, ({split.count_base(base) / split.len() * 100}%)")
        elif splitted[0] == "COMP":
            split = Seq(splitted[1])
            print(split.complement())
        elif splitted[0] == "REV":
            split = Seq(splitted[1])
            print(split.reverse())
        elif splitted[0] == "GENE":
            split = Seq()
            split.read_fasta(splitted[1])
            print(split.__str__())



        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

