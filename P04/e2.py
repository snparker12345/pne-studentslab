import socket
import termcolor

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

def process_client(cs):
    req_raw = cs.recv(1024)
    req = req_raw.decode()
    print("Message FROM CLIENT: ")

    # Split the request message into lines
    lines = req.split('\n')

    # Extract the request line
    req_line = lines[0]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # Check if the request is for /info/A
    if req_line.startswith("GET /info/A"):
        with open('info/A.html', 'rb') as f:
            content = f.read()
        # Send HTTP response with A.html content
        response_msg = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n".format(len(content)).encode() + content
    if req_line.startswith("GET /info/A"):
        with open('info/A.html', 'rb') as f:
            content = f.read()
        # Send HTTP response with A.html content
        response_msg = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n".format(len(content)).encode() + content
    else:
        # For any other request, send a blank response
        response_msg = "HTTP/1.1 200 OK\nContent-Length: 0\n\n".encode()

    # Send the response message back to the client
    cs.send(response_msg)

# Configure the server
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("Web server configured!")

# Main loop to accept incoming connections
try:
    while True:
        print("Waiting for clients....")
        try:
            (cs, client_ip_port) = ls.accept()
        except KeyboardInterrupt:
            print("Server stopped!")
            ls.close()
            exit()
        else:
            # Service the client
            process_client(cs)
            # Close the client socket
            cs.close()

except KeyboardInterrupt:
    print("Server stopped!")
    ls.close()
