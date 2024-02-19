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


def seq_len(seq):
    stuff = ['U5', 'ADA', 'FRAT1', 'FXN']
    # -- Constant with the new of the file to open
    length = len(seq)
    return length
    # print("Gene:", seq, "-> Length:", length)


def seq_count_base(sequence, base):
    # -- Constant with the new of the file to open
    # print("Gene", sequence, ":")
    dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    count = 0
    for letter in sequence:
        count += 1
        if letter in dnanums:
            val = dnanums.get(letter) + 1
            dnanums[letter] = val
    # print(base, dnanums.get(base))
    return dnanums.get(base)
    # print("A:", dnanums.get("A"))
    # print("C:", dnanums.get("C"))
    # print("T:", dnanums.get("T"))
    # print("G:", dnanums.get("G"), "\n")


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
    # f = "../sequences/" + seq
    # # -- Open and read the file
    # file_contents = Path(f).read_text()
    # file_contents = file_contents[file_contents.index('\n') + 1:]
    # file_contents = file_contents.replace("\n", "")
    # file_contents = file_contents[:20]
    # print("Fragment:", seq)
    revers = seq[::-1]
    # print("Reverse:", revers)
    return revers


def seq_complement(seq):
    # f = "../sequences/" + seq
    # # -- Open and read the file
    # file_contents = Path(f).read_text()
    # file_contents = file_contents[file_contents.index('\n') + 1:]
    # file_contents = file_contents.replace("\n", "")
    # file_contents = file_contents[:num]
    # print("Frag:", seq)
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'A')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'G')
    seq = seq.upper()
    return seq


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
