from scipy.special import comb

datafile = "../rosalind_data/rosalind_aspc.txt"

with open(datafile, 'r') as file:
    n, m = list(map(int, file.readline().split()))

MOD = 1000000
result = 0
    
# Sum C(n, k), where k range from m to n
for k in range(m, n + 1):
    result = (result + comb(n, k, exact=True)) % MOD
    
print(result)