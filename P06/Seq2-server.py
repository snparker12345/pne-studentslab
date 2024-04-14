import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from Seq1 import Seq

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        contents = ""

        path = self.path
        from urllib.parse import parse_qs, urlparse
        url_path = urlparse(self.path)
        path = url_path.path
        print("self path", self.path)
        if self.path.__contains__("myserver?ping="):
            contents = Path('html/ping.html').read_text()
            # we get it from here
        elif self.path.__contains__("sequence-button"):
            arguments = parse_qs(url_path.query)
            arg = arguments.get("operation")[0]
            file_contents = Path("../sequences/ADA.txt").read_text().split("\n")
            if (arg == "zero"):
                num = 0
                text = file_contents[1]
            elif (arg == "one"):
                num = 1
                text = file_contents[2]
            elif (arg == "two"):
                num = 2
                text = file_contents[3]
            elif (arg == "three"):
                num = 3
                text = file_contents[4]
            elif (arg == "four"):
                num = 4
                text = file_contents[5]
            contents = read_html_file("get.html").render(context={"todisplay": text, "otherdisplay": num})
        elif self.path.__contains__("gene-button"):
            arguments = parse_qs(url_path.query)
            arg = arguments.get("gene")[0]
            source = arg + ".txt"
            contents = Path("../sequences/" + source).read_text()
            lines = contents.split('\n')
            text = '\n'.join(lines[1:])
            contents = read_html_file("get.html").render(context={"todisplay": text, "otherdisplay": arg})
        elif self.path.__contains__("perform"):
            arguments = parse_qs(url_path.query)
            op = arguments.get("base")[0]
            seq = arguments.get("msg")[0]
            newSeq = Seq(seq)
            if op == "info":
                bases = "Total Length: " + str(seq.__len__()) + "\n"
                for base in "ATCG":
                    bases += f"{base}: {newSeq.count_base(base)}, ({newSeq.count_base(base) / newSeq.len() * 100}%)\n"
                res = bases
            elif op == "comp":
                res = newSeq.seq_complement(seq)
            elif op == "rev":
                res = newSeq.seq_reverse(seq)
            contents = read_html_file("operation.html").render(
                context={"sequence": seq, "operation": op, "result": res})
        elif path == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('html/index.html').read_text()
        else:
            contents = Path('html/error.html').read_text()
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
