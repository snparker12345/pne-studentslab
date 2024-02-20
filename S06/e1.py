class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.sequence = strbases
        self.valid_bases = {'A', 'C', 'G', 'T'}
        if all(base in self.valid_bases for base in strbases):
            print("New sequence created!")
        else:
            self.sequence = "ERROR"
            print("ERROR!!")


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


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

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
