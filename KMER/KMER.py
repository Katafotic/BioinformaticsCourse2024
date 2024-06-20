from Bio import SeqIO
import itertools

datafile = "../rosalind_data/rosalind_kmer.txt"


seq_string = []
with open (datafile,'r') as file:
    for seq_record in SeqIO.parse(file, 'fasta'):
        seq_string.append(str(seq_record.seq))

string = seq_string[0]
kmers = ["".join(x) for x in (itertools.product('ACGT', repeat = 4))]
seq = {i:0 for i in kmers}


for i in range(len(string) - 4 + 1):
    seq[string[i:i+4]] += 1
kmer = [seq[i] for i in kmers]
print(*kmer)