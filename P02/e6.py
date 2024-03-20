from Client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 6 |------")

IP = "127.0.0.1" # your IP address
PORT = 8080
c = Client(IP, PORT)

IP = "127.0.0.1" # your IP address
PORT2 = 8081
c2 = Client(IP, PORT2)
print(c2.__str__())

s3 = Seq()
s3 = s3.read_fasta("FRAT1.txt")
print("gene frat1", s3.__str__())

c.talk("sending frat1 gene to the server in fragments of 10 bases")
c2.talk("sending frat1 gene to the server in fragments of 10 bases")

substring = 0
substringfinal = 10
a = 0
for i in range(0, 10):
    gene = s3.__str__()
    substringtofind = gene[substring:substringfinal]
    print(substringtofind)
    substring += 10
    substringfinal += 10
    a += 1
    if i % 2 == 0:
        c.talk("fragment " + str(a) + ": " + substringtofind)
    else:
        c2.talk("fragment " + str(a) + ": " + substringtofind)

