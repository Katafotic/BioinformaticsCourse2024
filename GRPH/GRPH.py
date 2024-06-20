from Bio import SeqIO

datafile = "../rosalind_data/rosalind_grph.txt"

records = list(SeqIO.parse(datafile, "fasta"))
sequences = {record.id: str(record.seq) for record in records}

def find_overlap_adjacency_list(sequences, k=3):
    adjacency_list = []
    
    for id1, seq1 in sequences.items():
        suffix = seq1[-k:]
        for id2, seq2 in sequences.items():
            if id1 != id2 and seq2.startswith(suffix):
                adjacency_list.append((id1, id2))
    
    return adjacency_list

adjacency_list = find_overlap_adjacency_list(sequences)
# print(adjacency_list)

for edge in adjacency_list:
    print(edge[0], edge[1])
