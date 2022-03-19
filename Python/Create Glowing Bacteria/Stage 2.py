class Strand:
    def __init__(self, strand):
        self.strand = strand
        self.bases = {'A': 'T',
                      'T': 'A',
                      'C': 'G',
                      'G': 'C'}
    
    def get_complementary(self):
        return ''.join(self.bases[e] for e in self.strand)

    def _insert(self, strand, pos):
        return f'{strand[:pos]} {strand[pos:]}'

    def cut(self, site):
        comp_strand = self.get_complementary()
        spos, slen = self.strand.index(site), len(site)
        return (self._insert(self.strand, spos+1),
                self._insert(comp_strand, spos+slen-1))

    
def main():
    strand = 'GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTTATTTGTATAGTTCA'
    strand = Strand(strand)
    print('\n'.join(strand.cut('CTGCAG')))

if __name__ == '__main__':
    main()
