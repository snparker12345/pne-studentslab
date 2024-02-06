dnanums = {'A': 0, 'C':0, 'T':0, 'G':0}
filename = input("enter the filename: ")
line_count = 0
with open(filename, "r") as stuff:
    lines = stuff.readlines()
    for line in lines:
        line_count += 1
        for letter in line:
            if letter in dnanums:
                val = dnanums.get(letter) + 1
                dnanums[letter] = val
    print("Total length:", line_count)
    print("A: ", dnanums.get("A"))
    print("C: ", dnanums.get("C"))
    print("T: ", dnanums.get("T"))
    print("G: ", dnanums.get("G"))