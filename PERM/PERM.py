import itertools

datafile = "../rosalind_data/rosalind_perm.txt"

with open(datafile, 'r') as file:
    n = int(file.read())

permutations = list(itertools.permutations(range(1, n + 1)))
total_permutations = len(permutations)
    
print(total_permutations)
    
for perm in permutations:
    print(" ".join(map(str, perm)))
