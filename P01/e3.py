class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        valid_bases = set("ATCG")
        if strbases is None:
            self.strbases = None
            print("NULL sequence created")
        elif all(base in valid_bases for base in strbases) == 1:
            self.strbases = strbases
            print("Valid sequence created!")
        else:
            self.strbases = strbases
            print("INVALID sequence!")

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
        """Calculate the length of the sequence"""
        if self.strbases is None:
            return 0
        else:
            return len(self.strbases)


# Create a null sequence
s1 = Seq()

# Create a valid sequence
s2 = Seq("ACTGA")

# Create an invalid sequence
s3 = Seq("Invalid sequence")

# Print the sequences
print("Sequence 1:", s1)
print("Sequence 2:", s2)
print("Sequence 3:", s3)
