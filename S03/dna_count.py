filename = input("enter the filename: ")

with (open(filename, "r") as stuff):
    final_string = ""
    final_string += stuff.readline()
    dnanums = {'A': 0, 'C':0, 'T':0, 'G':0}
    numchars = len(final_string)
    print(numchars)
    for i in final_string:
        if i in dnanums:
            val = dnanums.get(i) + 1
            dnanums[i] = val
    print("A: ", dnanums.get("A"))
    print("C: ", dnanums.get("C"))
    print("T: ", dnanums.get("T"))
    print("G: ", dnanums.get("G"))
