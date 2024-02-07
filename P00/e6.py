from pathlib import Path

print("-----| Exercise 6 |------\n")

seq = input("DNA file:")
num = input("Number of chars:")


def seq_reverse(seq, num):
    f = "../sequences/" + seq
    # -- Open and read the file
    file_contents = Path(f).read_text()
    file_contents = file_contents[file_contents.index('\n') + 1:]
    file_contents = file_contents.replace("\n", "")
    file_contents = slice(0, num)
    print(file_contents)
    revers = file_contents[::-1]
    print(revers)

seq_reverse(seq, num)