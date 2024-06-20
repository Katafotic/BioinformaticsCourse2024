from Bio import SeqIO

datafile = "../rosalind_data/rosalind_tran.txt"

seq_string = []
with open (datafile,'r') as file:
    for seq_record in SeqIO.parse(file, 'fasta'):
        seq_string.append(str(seq_record.seq))
s1, s2 = seq_string[0], seq_string[1]

def transition_transversion_ratio(s1, s2):
    transitions = 0
    transversions = 0
    
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}
    
    for nt1, nt2 in zip(s1, s2):
        if nt1 != nt2:
            if nt1 in purines and nt2 in purines:
                transitions += 1
            elif nt1 in pyrimidines and nt2 in pyrimidines:
                transitions += 1
            else:
                transversions += 1
    
    return transitions / transversions

print(transition_transversion_ratio(s1, s2))