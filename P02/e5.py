from Client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 6 |------")

IP = "212.128.255.66" # your IP address
PORT = 8080
c = Client(IP, PORT)
print(c.__str__())

s3 = Seq()
s3 = s3.read_fasta("FRAT1.txt")
print("gene frat1", s3.__str__())
c.talk("sending frat1 gene to the server in fragments of 10 bases")

substring = 0
substringfinal = 10
for i in range(0, 5):
    gene = s3.__str__()
    substringtofind = gene[substring:substringfinal]
    print(substringtofind)
    substring += 10
    substringfinal += 10
    c.talk(substringtofind)
