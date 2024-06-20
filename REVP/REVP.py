from Bio import SeqIO

datafile = "../rosalind_data/rosalind_revp.txt"

for record in SeqIO.parse(datafile, "fasta"):
    sequence = str(record.seq)


def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna_sequence))

def find_reverse_palindromes(dna_sequence):
    reverse_palindromes = []
    n = len(dna_sequence)
    
    for length in range(4, 13):
        for start in range(n - length + 1):
            substring = dna_sequence[start:start+length]
            if substring == reverse_complement(substring):
                reverse_palindromes.append((start + 1, length))  # Convert to 1-based index
    
    return reverse_palindromes


reverse_palindromes = find_reverse_palindromes(sequence)
for pos, length in reverse_palindromes:
    print(pos, length)