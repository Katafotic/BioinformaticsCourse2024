datafile = "../rosalind_data/rosalind_mrna.txt"

with open(datafile, 'r') as file:
    data = file.read().strip()
    
def count_rna_strings(protein_string):
    genetic_code = {
        'F': ['UUU', 'UUC'],
        'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'I': ['AUU', 'AUC', 'AUA'],
        'M': ['AUG'],
        'V': ['GUU', 'GUC', 'GUA', 'GUG'],
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
        'P': ['CCU', 'CCC', 'CCA', 'CCG'],
        'T': ['ACU', 'ACC', 'ACA', 'ACG'],
        'A': ['GCU', 'GCC', 'GCA', 'GCG'],
        'Y': ['UAU', 'UAC'],
        'H': ['CAU', 'CAC'],
        'Q': ['CAA', 'CAG'],
        'N': ['AAU', 'AAC'],
        'K': ['AAA', 'AAG'],
        'D': ['GAU', 'GAC'],
        'E': ['GAA', 'GAG'],
        'C': ['UGU', 'UGC'],
        'W': ['UGG'],
        'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'G': ['GGU', 'GGC', 'GGA', 'GGG'],
        '*': ['UAA', 'UAG', 'UGA']
    }
    
    count = 1
    
    for aa in protein_string:
        count *= len(genetic_code[aa])
        count %= 1000000  # prevent overflow
    
    count *= 3
    count %= 1000000  # prevent overflow
    
    return count

result = count_rna_strings(data)
print(result)
