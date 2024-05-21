import http.client
import json
import termcolor
from pydoc import html
from Seq0 import *
from P03.Seq0 import Seq


SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/species/'
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

species_data = response.json()['species']

species_names = [species["name"] for species in species_data]

# Print the list of species names
print(species_names)
aliases_list = []

for species in species_data:
    aliases_list.extend(species.get('aliases', []))