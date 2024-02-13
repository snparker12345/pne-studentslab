from pathlib import Path


def seq_count_base():
    print("-----| Exercise 4 |------\n")

    stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
    # -- Constant with the new of the file to open
    for s in stuff:
        FILENAME = "../sequences/" + s + ".txt"
        file_contents = Path(FILENAME).read_text()
        file_contents = file_contents[file_contents.index('\n') + 1:]
        file_contents = file_contents.replace("\n", "")
        print("Gene", s, ":")
        dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        count = 0
        for letter in file_contents:
            count += 1
            if letter in dnanums:
                val = dnanums.get(letter) + 1
                dnanums[letter] = val
        print("A:", dnanums.get("A"))
        print("C:", dnanums.get("C"))
        print("T:", dnanums.get("T"))
        print("G:", dnanums.get("G"), "\n")
