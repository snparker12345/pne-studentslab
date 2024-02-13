from pathlib import Path

print("-----| Exercise 7 |------")


def seq_reverse(seq, num):
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
# seq = input("DNA file:")
# num = int(input("Number of chars:"))
print("Gene U5:")
seq_reverse("U5.txt", 20)