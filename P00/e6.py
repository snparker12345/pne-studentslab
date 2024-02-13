from pathlib import Path

print("-----| Exercise 6 |------")


def seq_reverse(seq, num):
    f = "../sequences/" + seq
    # -- Open and read the file
    file_contents = Path(f).read_text()
    file_contents = file_contents[file_contents.index('\n') + 1:]
    file_contents = file_contents.replace("\n", "")
    file_contents = file_contents[:num]
    print("Fragment:", file_contents)
    revers = file_contents[::-1]
    print("Reverse:", revers)


# seq = input("DNA file:")
# num = int(input("Number of chars:"))
print("Gene U5:")
seq_reverse("U5.txt", 20)
