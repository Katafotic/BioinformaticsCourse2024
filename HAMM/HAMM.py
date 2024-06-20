import sys

count = 0
seq1, seq2 = sys.stdin.readlines()
for nucleotide_1, nucleotide_2 in zip(seq1, seq2):
    if (nucleotide_1 != nucleotide_2):
        count += 1

print(count)