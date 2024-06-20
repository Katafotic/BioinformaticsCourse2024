from Bio import SeqIO

datafile = "../rosalind_data/rosalind_kmp.txt"

for record in SeqIO.parse(datafile, "fasta"):
    sequence = str(record.seq)


def compute_failure_array(s):
    n = len(s)
    F = [0] * n
    j = 0
    
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = F[j - 1]
        if s[i] == s[j]:
            j += 1
            F[i] = j
    
    return F


failure_array = compute_failure_array(sequence)
print(*failure_array)
