from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

file_contents = file_contents.split("\n")
print("Body of the U5.txt file:")
lineval = 0
for line in file_contents:
    if lineval != 0:
        print(line)
    lineval += 1


