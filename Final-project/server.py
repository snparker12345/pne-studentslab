import http.server
import socketserver
import termcolor
import jinja2 as j
import http.client
import json
from Seq0 import *

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

def get_species():
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/info/species/'
    PARAMS = '?content-type=application/json'
    print(f"Server: {SERVER}")
    request = ENDPOINT + PARAMS
    url = SERVER + ENDPOINT + PARAMS

    print()

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

        # -- Read the response message from the server
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    response = json.loads(r1.read().decode("utf-8"))

    if r1.status == 400:
        return None
    species_data = response['species']

    species_names = [species["name"] for species in species_data]

    # Print the list of species names
    # print(species_names)
    return species_names

def get_karyotype(specie):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/info/assembly/'
    PARAMS = '?content-type=application/json'
    print(f"Server: {SERVER}")
    request = ENDPOINT + specie + PARAMS
    url = SERVER + ENDPOINT + specie + PARAMS

    print()

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

        # -- Read the response message from the server
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.status == 400:
        return None

    # -- Read the response's body
    response = json.loads(r1.read().decode("utf-8"))

    karyotype_data = response['karyotype']

    # Print the list of species names
    # print(species_names)
    return karyotype_data

def get_chromosome_length(specie, chrom):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/info/assembly/'
    PARAMS = '?content-type=application/json'
    print(f"Server: {SERVER}")
    request = ENDPOINT + specie + PARAMS
    url = SERVER + ENDPOINT + specie + PARAMS

    print()

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

        # -- Read the response message from the server
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.status == 400:
        return None
    else:
    # -- Read the response's body
        response = json.loads(r1.read().decode("utf-8"))

        chromosome_data = response['top_level_region']

        for chromosome in chromosome_data:
            if chromosome.get("name") == chrom:
                return chromosome.get("length")
            else:
                return None
def get_gene(gene):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/xrefs/symbol/'
    SPECIE = 'homo_sapiens/'
    PARAMS = '?content-type=application/json'
    print(f"Server: {SERVER}")
    request = ENDPOINT + SPECIE + gene + PARAMS
    url = SERVER + ENDPOINT + SPECIE + gene + PARAMS

    print()

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

        # -- Read the response message from the server
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.status == 400:
        return None
    else:
    # -- Read the response's body
        response = json.loads(r1.read().decode("utf-8"))
        gene_name = response[0]
        gotten_gene = gene_name.get("id")
        if gotten_gene is None:
            return None
        else:
            return gotten_gene


def get_seq(id):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/sequence/id/'
    PARAMS = '?content-type=application/json'
    print(f"Server: {SERVER}")
    request = ENDPOINT + id + PARAMS
    url = SERVER + ENDPOINT + id + PARAMS

    print()

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    response = json.loads(r1.read().decode("utf-8"))
    seq = response['seq']

    return seq


def get_gene_info(gene):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/lookup/id/'
    PARAMS = '?content-type=application/json'
    print(f"Server: {SERVER}")
    request = ENDPOINT + gene + PARAMS
    url = SERVER + ENDPOINT + gene + PARAMS

    print()

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

        # -- Read the response message from the server
    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.status == 400:
        return None
    else:
        # -- Read the response's body
        response = json.loads(r1.read().decode("utf-8"))
        start = response.get('start')
        end = response.get('end')
        chrom = response.get('seq_region_name')
        info = [start, end, chrom]
        return info

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

        if self.path.__contains__("listSpecies"):
            arguments = parse_qs(url_path.query)
            limit = arguments.get("limit")[0]
            species = get_species()
            if species is None:
                contents = Path('html/error.html').read_text()
            else:
                num = len(species)
                if limit is not None:
                    limit = int(limit)
                    species = species[:limit]
                species_list = ""
                for specie in species:
                    species_list += f"<li>{specie}</li>"
                contents = read_html_file("species.html").render(
                    context={"species": species_list, "num": num, "limit": limit})
                # make each word have a * and then submit into the html

        elif self.path.__contains__("karyotype"):
            arguments = parse_qs(url_path.query)
            id = arguments.get("speciesK")[0]
            karyotype_list = get_karyotype(id)
            if karyotype_list is None:
                contents = Path('html/error.html').read_text()
            else:
                karyotypes = ""
                for specie in karyotype_list:
                    karyotypes += f"<li>{specie}</li>"
                contents = read_html_file("karyotype.html").render(
                    context={"chromosomeList": karyotypes})
            # we get it from here

        elif self.path.__contains__("chromosomeLength"):
            arguments = parse_qs(url_path.query)
            specie = arguments.get("speciesL")[0]
            chrom = arguments.get("chromosome")[0]
            chrom_len = get_chromosome_length(specie, chrom)
            if (chrom_len is None):
                contents = Path('html/error.html').read_text()
            else:
                contents = read_html_file("length.html").render(context={"chromosomeLength": chrom_len})

        elif self.path.__contains__("geneSeq"):
            arguments = parse_qs(url_path.query)
            geneToGet = arguments.get("gene")[0]
            gotten_gene = get_gene(geneToGet)
            if gotten_gene is None:
                contents = Path('html/error.html').read_text()
            else:
                seq = get_seq(gotten_gene)
                contents = read_html_file("seq.html").render(context={"gene": geneToGet, "seq":seq})

        elif self.path.__contains__("geneInfo"):
            arguments = parse_qs(url_path.query)
            gene_to_get = arguments.get("geneI")[0]
            gotten_gene = get_gene(gene_to_get)
            seq = get_seq(gotten_gene)
            length = len(seq)
            info = get_gene_info(gotten_gene)
            start = info[0]
            end = info[1]
            chromosome = info[2]
            contents = read_html_file("gene_info.html").render(context={"start": start, "end": end, "length": length, "chromosome": chromosome, "id":gotten_gene})

        elif self.path.__contains__("geneCalc"):
            arguments = parse_qs(url_path.query)
            gene_to_get = arguments.get("geneI")[0]
            gotten_gene = get_gene(gene_to_get)
            seq = get_seq(gotten_gene)
            length = len(seq)
            for base in "ATCG":
                bases = f"{base}: {seq.count_base(base)}, ({seq.count_base(base) / seq.len() * 100}%)"


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
