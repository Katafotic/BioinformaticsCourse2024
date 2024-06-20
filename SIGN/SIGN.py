from itertools import permutations, product


datafile = "../rosalind_data/rosalind_sign.txt"

with open(datafile, 'r') as file:
    n = int(file.read())


base_permutations = permutations(range(1, n+1))
    
all_signed_perms = []
    
for perm in base_permutations:
    for signs in product([-1, 1], repeat=n):
        signed_perm = [a * b for a, b in zip(perm, signs)]
        all_signed_perms.append(signed_perm)
    

total_count = len(all_signed_perms)
    
print(total_count)
    
for perm in all_signed_perms:
    print(' '.join(map(str, perm)))
