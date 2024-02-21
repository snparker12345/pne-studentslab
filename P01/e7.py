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

print("-----| Practice 1, Exercise 7 |------")

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print(f"  Bases: {s1.count()}")
print(f"  Rev:   {s1.reverse()}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"  Bases: {s2.count()}")
print(f"  Rev:   {s2.reverse()}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print(f"  Bases: {s3.count()}")
print(f"  Rev:   {s3.reverse()}")
