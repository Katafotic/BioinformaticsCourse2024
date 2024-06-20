from Bio import SeqIO
from scipy.special import factorial

datafile = "../rosalind_data/rosalind_pmch.txt"

for record in SeqIO.parse(datafile, "fasta"):
    sequence = str(record.seq)

a, c = sequence.count("A"), sequence.count("C")
print(f"perfect_matching = {a}! * {c}!")

factorial_a = factorial(a, exact=True)
factorial_c = factorial(c, exact=True)

perfect_matchings = factorial_a * factorial_c

print(perfect_matchings)
