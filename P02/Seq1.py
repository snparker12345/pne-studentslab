from pathlib import Path

import termcolor


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = None
            return
        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


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


class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """

    def __init__(self, strbases, name=""):
        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")


def print_seqs(seq_list, color):
    for i, seq in enumerate(seq_list):
        termcolor.cprint(f"Sequence {i}: (Length: {seq.len()}) {seq}", color)

def generate_seqs(pat, num):
    seq_list = []
    for i in range(1, num + 1):
        seq_list.append(Seq(pat * i))
    return seq_list

