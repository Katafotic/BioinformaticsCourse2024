import itertools

datafile = "../rosalind_data/rosalind_lexf.txt"

with open(datafile, 'r') as file:
    alphabet = file.readline().split()
    n = int(file.read())



combinations = itertools.product(alphabet, repeat=n)
sorted_combinations = sorted(combinations)
    
for comb in sorted_combinations:
    print(''.join(comb))