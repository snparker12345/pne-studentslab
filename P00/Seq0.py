from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    # -- Constant with the new of the file to open
    f = "../sequences/" + filename
    print("DNA file: U5.txt")
    print("The first 20 bases are:")
    # -- Open and read the file
    file_contents = Path(f).read_text()
    file_contents = file_contents[file_contents.index('\n') + 1:]
    file_contents = file_contents.replace("\n", "")
    print(file_contents[:20])


def seq_len():
    stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
    # -- Constant with the new of the file to open
    for s in stuff:
        FILENAME = "../sequences/" + s + ".txt"
        file_contents = Path(FILENAME).read_text()
        file_contents = file_contents[file_contents.index('\n') + 1:]
        file_contents = file_contents.replace("\n", "")
        length = len(file_contents)
        print("Gene:", s, "-> Length:", length)


def seq_count_base():
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


def seq_count():
    stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
    # -- Constant with the new of the file to open
    for s in stuff:
        FILENAME = "../sequences/" + s + ".txt"
        file_contents = Path(FILENAME).read_text()
        file_contents = file_contents[file_contents.index('\n') + 1:]
        file_contents = file_contents.replace("\n", "")

        dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        count = 0
        for letter in file_contents:
            count += 1
            if letter in dnanums:
                val = dnanums.get(letter) + 1
                dnanums[letter] = val
        print("Gene", s, ":", dnanums)


def seq_reverse(seq):
    f = "../sequences/" + seq
    # -- Open and read the file
    file_contents = Path(f).read_text()
    file_contents = file_contents[file_contents.index('\n') + 1:]
    file_contents = file_contents.replace("\n", "")
    file_contents = file_contents[:20]
    print("Fragment:", file_contents)
    revers = file_contents[::-1]
    print("Reverse:", revers)


def seq_complement(seq, num):
    f = "../sequences/" + seq
    # -- Open and read the file
    file_contents = Path(f).read_text()
    file_contents = file_contents[file_contents.index('\n') + 1:]
    file_contents = file_contents.replace("\n", "")
    file_contents = file_contents[:num]
    print("Frag:", file_contents)
    file_contents = file_contents.replace('A', 't')
    file_contents = file_contents.replace('T', 'A')
    file_contents = file_contents.replace('G', 'c')
    file_contents = file_contents.replace('C', 'G')
    file_contents = file_contents.upper()
    print("Comp:", file_contents)


def ex_eight():
    stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
    # -- Constant with the new of the file to open
    for s in stuff:
        FILENAME = "../sequences/" + s + ".txt"
        file_contents = Path(FILENAME).read_text()
        file_contents = file_contents[file_contents.index('\n') + 1:]
        file_contents = file_contents.replace("\n", "")
        dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        count = 0
        for letter in file_contents:
            count += 1
            if letter in dnanums:
                val = dnanums.get(letter) + 1
                dnanums[letter] = val
        key_max = max(zip(dnanums.values(), dnanums.keys()))[1]
        print("Gene", s, ":", "Most frequent Base:", key_max)
