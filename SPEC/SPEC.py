from Bio import SeqIO

datafile = "../rosalind_data/rosalind_spec.txt"

masses = []
with open(datafile, 'r') as file:
    for mass in file.readlines():
        masses.append(float(mass))

mass_table = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


protein_string = ''
mass_to_aa = {round(mass, 5): aa for aa, mass in mass_table.items()}
    
for i in range(1, len(masses)):
    diff = round(masses[i] - masses[i - 1], 5)
    if diff in mass_to_aa:
        protein_string += mass_to_aa[diff]
print(protein_string)