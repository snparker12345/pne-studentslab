from Client0 import Client
from Seq1 import Seq





IP = "212.128.255.66" # your IP address
PORT = 8080
print("-----| Practice 2, Exercise 4 |------")
c = Client(IP, PORT)
print(c)

s1 = Seq()
s1 = s1.read_fasta("U5.txt")
print("to server:", s1.__str__())
print("from server...")
c.talk(s1.__str__())
response = c.talk("Testing!!!")
print(response)


s2 = Seq()
s2 = s2.read_fasta("ADA.txt")
print("to server:", s2.__str__())
c.talk(s2.__str__())
response = c.talk("Te")
print("from server...")
print(response)


s3 = Seq()
s3 = s3.read_fasta("FRAT1.txt")
print("to server:", s3.__str__())
print("from server...")
c.talk(s1.__str__())
response = c.talk("Testing!!!")
print(response)


s4 = Seq()
s4 = s4.read_fasta("FXN.txt")
print("to server:", s4.__str__())
print("from server...")
c.talk(s4.__str__())
response = c.talk("Testing!!!")
print(response)


s5 = Seq()
s5 = s5.read_fasta("RNU6_269P.txt")
print("to server:", s5.__str__())
print("from server...")
response = c.talk("Testing!!!")
c.talk(s5.__str__())
print(response)
