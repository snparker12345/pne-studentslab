from pathlib import Path

filename = input("DNA file:")

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



seq_read_fasta(filename)