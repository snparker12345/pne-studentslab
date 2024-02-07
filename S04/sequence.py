from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../sequences/ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

file_contents = file_contents.split("\n")

print("Body of the U5.txt file:")
length = 0
linenum = 0
for line in file_contents:
    if linenum != 0:
        print(line)
        length += len(line)
    linenum += 1
print(length)
