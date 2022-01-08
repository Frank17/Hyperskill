class Strand:
    def __init__(self, strand):
        self.strand = strand
        self.bases = {'A': 'T',
                      'T': 'A',
                      'C': 'G',
                      'G': 'C'}
    
    def get_complementary(self):
        return ''.join(self.bases[e] for e in self.strand)


strand = 'GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTGTGCACTACCTCCTT'
strand = Strand(strand)
print(strand.get_complementary())
