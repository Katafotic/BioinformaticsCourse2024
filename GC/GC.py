from Bio import SeqIO
from Bio.SeqUtils import GC

best_read, max_GC = None, 0


filename = "../rosalind_data/rosalind_gc.txt"

with open(filename, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        if max_GC < GC(record.seq):
            best_read = record.id
            max_GC = GC(record.seq)


print(f"{best_read}\n{max_GC}")
