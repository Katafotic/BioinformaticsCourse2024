from Bio import SeqIO

datafile = "../rosalind_data/rosalind_pdst.txt"

sequences = []
with open(datafile, 'r') as file:
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(str(record.seq))


def p_distance(seq1, seq2):
    length = len(seq1)
    mismatches = sum(1 for i in range(length) if seq1[i] != seq2[i])
    return mismatches / length

def compute_distance_matrix(sequences):
    n = len(sequences)
    D = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            dist = p_distance(sequences[i], sequences[j])
            D[i][j] = dist
            D[j][i] = dist
    
    return D

D = compute_distance_matrix(sequences)

for row in D:
    print(*row)