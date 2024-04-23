
import http.client
import json
import termcolor
from pydoc import html

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/ENSG00000207552'
PARAMS = '?content-type=application/json'
REQUEST = ENDPOINT + PARAMS
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", REQUEST)
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
print("MIR633")
termcolor.cprint("Description: ", "green")
print(response["desc"])
termcolor.cprint("Bases: ", "green")
print(response["seq"])
#pinged = response.__contains__("ping: 1")


# -- Create a variable with the data,
# -- form the JSON received