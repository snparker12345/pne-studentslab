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
            send_bytes = str.encode(response)
            # We must write bytes, not a string
            ls.send(send_bytes)
            print("OK")
        elif splitted[0] == "GET":
            num = int(splitted[1])
            print("GET")
            print(seq_list[num])
            send_bytes = str.encode(seq_list[num])
            ls.send(send_bytes)
        elif splitted[0] == "INFO":
            split = Seq(splitted[1])
            seq = f"Sequence:{splitted[1]}"
            print(seq)
            ls.send(str.encode(seq))
            len = f"Length: {split.len()}"
            print(len)
            ls.send(str.encode(len))
            for base in "ATCG":
                bases = f"{base}: {split.count_base(base)}, ({split.count_base(base) / split.len() * 100}%)"
                print(bases)
                ls.send(str.encode(bases))
        elif splitted[0] == "COMP":
            split = Seq(splitted[1])
            sl = split.complement()
            print(sl)
            ls.send(str.encode(sl))
        elif splitted[0] == "REV":
            split = Seq(splitted[1])
            rev = split.reverse()
            print(rev)
            ls.send(str.encode(rev))
        elif splitted[0] == "GENE":
            split = Seq()
            gene = split.__str__()
            split.read_fasta(splitted[1])
            print(gene)
            ls.send(gene)




        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

