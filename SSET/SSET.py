datafile = "../rosalind_data/rosalind_sset.txt"

with open(datafile, 'r') as file:
    n = int(file.readline())


MOD = 1000000

def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

print(modular_exponentiation(2, n, MOD))
