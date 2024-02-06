dnanums = {'A': 0, 'C':0, 'T':0, 'G':0}
count = 0
line = input("Introduce the sequence: ")
for letter in line:
    count += 1
    if letter in dnanums:
        val = dnanums.get(letter) + 1
        dnanums[letter] = val

print("Total length:", count)
print("A: ", dnanums.get("A"))
print("C: ", dnanums.get("C"))
print("T: ", dnanums.get("T"))
print("G: ", dnanums.get("G"))