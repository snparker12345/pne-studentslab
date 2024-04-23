import http.client
import json
import termcolor
from pydoc import html
from Seq0 import *
from P03.Seq0 import Seq

genes_list = {'FRAT1':'ENSG00000165879', 'ADA':'ENSG00000196839', 'FXN':"ENSG00000165060", 'RNU6_269P':"ENSG00000212379", 'MIR633':"ENSG00000207552", 'TTTY4C':"ENSG00000228296", 'RBMY2YP':"ENSG00000227633", 'FGFR3':"ENSG00000068078", 'KDR':"ENSG00000128052", 'ANK2':"ENSG00000145362"}




for gene in genes_list:
    id = genes_list[gene]

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
    #print(f"Response received!: {response}\n")
    termcolor.cprint("Gene: ", "green")
    print(gene)
    termcolor.cprint("Description: ", "green")
    print(response["desc"])
    seq = response["seq"]
    s = Seq(seq)
    termcolor.cprint("Total length: ", "green")
    print(s.len())
    for base in "ATCG":
        bases = f"{base}: {s.count_base(base)}, ({s.count_base(base) / s.len() * 100}%)"
        print(bases)
    dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    count = 0
    for letter in seq:
        count += 1
        if letter in dnanums:
            val = dnanums.get(letter) + 1
            dnanums[letter] = val
    key_max = max(zip(dnanums.values(), dnanums.keys()))[1]
    print("Most frequent Base:", key_max)
    #pinged = response.__contains__("ping: 1")


    # -- Create a variable with the data,
    # -- form the JSON received