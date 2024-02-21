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
        valid_bases = set("ATCG")
        """Calculate the length of the sequence"""
        if self.strbases is None or all(base in valid_bases for base in self.strbases) == 0:
            return 0
        else:
            return len(self.strbases)




s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
