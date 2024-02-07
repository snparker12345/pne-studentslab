from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../sequences/U5.txt"
print("DNA file: U5.txt")
print("The first 20 bases are:")
# -- Open and read the file
file_contents = Path(FILENAME).read_text()
file_contents = file_contents[file_contents.index('\n')+1:]
file_contents = file_contents.replace("\n", "")
print(file_contents[:20])
