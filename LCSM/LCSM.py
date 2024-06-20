from Bio import SeqIO

datafile = "../rosalind_data/rosalind_lcsm.txt"

sequences = []
for record in SeqIO.parse(datafile, "fasta"):
    sequences.append(str(record.seq))

def is_common_substring(sequences, length):
    if length == 0:
        return True
    
    substrings = set()
    
    first_sequence = sequences[0]
    for i in range(len(first_sequence) - length + 1):
        substrings.add(first_sequence[i:i+length])
    
    for seq in sequences[1:]:
        found = False
        for sub in substrings:
            if sub in seq:
                found = True
                break
        if not found:
            return False
            
    return True

def LCS(sequences):
    if not sequences:
        return ""
    
    low, high = 0, min(len(seq) for seq in sequences)
    best_length = 0
    
    while low <= high:
        mid = (low + high) // 2
        if is_common_substring(sequences, mid):
            best_length = mid
            low = mid + 1
        else:
            high = mid - 1
    
    substrings = set()
    first_sequence = sequences[0]
    for i in range(len(first_sequence) - best_length + 1):
        substrings.add(first_sequence[i:i+best_length])
    
    for sub in substrings:
        if all(sub in seq for seq in sequences):
            return sub
    
    return ""

print(LCS(sequences))