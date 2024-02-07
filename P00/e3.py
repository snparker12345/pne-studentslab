from pathlib import Path

stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
# -- Constant with the new of the file to open
for s in stuff:
    FILENAME = "../sequences/" + s + ".txt"
    file_contents = Path(FILENAME).read_text()
    file_contents = file_contents[file_contents.index('\n')+1:]
    file_contents = file_contents.replace("\n", "")
    length = len(file_contents)
    print("Gene:", s, "-> Length:", length)
