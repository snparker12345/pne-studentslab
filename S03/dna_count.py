stuff = input("introduce the sequence: ")
dnanums = {'A': 0, 'C':0, 'T':0, 'G':0}
numchars = len(stuff)
print(numchars)
for i in stuff:
    if i in dnanums:
        val = dnanums.get(i) + 1
        dnanums[i] = val
print("A: ", dnanums.get("A"))
print("C: ", dnanums.get("C"))
print("T: ", dnanums.get("T"))
print("G: ", dnanums.get("G"))
