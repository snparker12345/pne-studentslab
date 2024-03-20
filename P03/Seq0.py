from pathlib import Path


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        valid_bases = set("ATCG")
        if strbases is None:
            self.strbases = None
            print("NULL sequence created")
        elif all(base in valid_bases for base in strbases) == 1:
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = strbases
            print("INVALID sequence!")

    def read_fasta(self, filename):
        try:
            f = "../sequences/" + filename
            file_contents = Path(f).read_text()
            file_contents = file_contents[file_contents.index('\n') + 1:]
            file_contents = file_contents.replace("\n", "")
            self.strbases = file_contents
        except FileNotFoundError:
            print("File not found.")
        return self

    def __str__(self):
        """Method called when the object is being printed"""
        valid_bases = set("ATCG")
        if self.strbases is None:
            return "NULL"
        elif all(base in valid_bases for base in self.strbases) == 0:
            return "ERROR"
        else:
            return self.strbases

    def len(self):
        valid_bases = set("ATCG")
        """Calculate the length of the sequence"""
        if self.strbases is None or all(base in valid_bases for base in self.strbases) == 0:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.__str__() == "ERROR":
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.len() == 0:
            return bases
        for base in self.strbases:
            if base in bases:
                bases[base] += 1
        return bases

    def reverse(self):
        if self.len() == 0:
            return self.__str__()
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.len() == 0:
            return self.__str__()
        s = self.strbases
        s = s.replace('A', 't')
        s = s.replace('T', 'A')
        s = s.replace('G', 'c')
        s = s.replace('C', 'G')
        s = s.upper()
        return s

    def ex_eight(self, filename):
        dnanums = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        count = 0
        for letter in self.strbases:
            count += 1
            if letter in dnanums:
                val = dnanums.get(letter) + 1
                dnanums[letter] = val
        key_max = max(zip(dnanums.values(), dnanums.keys()))[1]
        print(filename, ": Most frequent Base:", key_max)