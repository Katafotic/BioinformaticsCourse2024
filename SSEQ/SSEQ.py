from Bio import SeqIO

datafile = "../rosalind_data/rosalind_sseq.txt"

sequences = []
with open(datafile, 'r') as file:
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(str(record.seq))
s1, s2 = sequences[0], sequences[1]


indices = []
s1_index = 0

for char in s2:
    s1_index = s1.find(char, s1_index)
    indices.append(s1_index + 1)
    s1_index += 1 

print(' '.join(map(str, indices)))
