from Bio import SeqIO


datafile = "../rosalind_data/rosalind_cons.txt"
sequences = []
for record in SeqIO.parse(datafile, "fasta"):
    sequences.append(str(record.seq))


def create_profile_matrix(sequences):
    length = len(sequences[0])
    profile = {'A': [0] * length, 'C': [0] * length, 'G': [0] * length, 'T': [0] * length}
    
    for sequence in sequences:
        for i, nucleotide in enumerate(sequence):
            profile[nucleotide][i] += 1
    
    return profile

def generate_consensus_string(profile):
    consensus = []
    for i in range(len(profile['A'])):
        column = {nucleotide: profile[nucleotide][i] for nucleotide in 'ACGT'}
        max_nucleotide = max(column, key=column.get)
        consensus.append(max_nucleotide)
    return ''.join(consensus)


profile = create_profile_matrix(sequences)
consensus = generate_consensus_string(profile)

print(consensus)
for nucleotide in "ACGT":
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")

