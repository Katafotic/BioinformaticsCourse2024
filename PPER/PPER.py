datafile = "../rosalind_data/rosalind_pper.txt"

with open(datafile, 'r') as file:
    n, k = list(map(int, file.readline().split()))

MOD = 1000000

result = 1
for i in range(n, n-k, -1):
    result = (result * i) % MOD

print(result)