print("-----| Exercise 5 |------\n")

from pathlib import Path

stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
# -- Constant with the new of the file to open
for s in stuff:
    FILENAME = "../sequences/" + s + ".txt"
    file_contents = Path(FILENAME).read_text()
    file_contents = file_contents[file_contents.index('\n')+1:]
    file_contents = file_contents.replace("\n", "")

    dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    count = 0
    for letter in file_contents:
        count += 1
        if letter in dnanums:
            val = dnanums.get(letter) + 1
            dnanums[letter] = val
    print("Gene", s, ":", dnanums)
