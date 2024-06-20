datafile = "../rosalind_data/rosalind_lgis.txt"

with open(datafile, 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))


def longest_increasing_subsequence(n, permutation):
    if n == 0:
        return []
    
    dp_inc = [1] * n 
    prev = [-1] * n 

    for i in range(1, n):
        for j in range(0, i):
            if permutation[j] < permutation[i]:
                if dp_inc[j] + 1 > dp_inc[i]:
                    dp_inc[i] = dp_inc[j] + 1
                    prev[i] = j

    max_len_inc = max(dp_inc)
    
    lis = []
    idx = dp_inc.index(max_len_inc)
    while idx != -1:
        lis.append(permutation[idx])
        idx = prev[idx]

    lis.reverse()
    return lis

def longest_decreasing_subsequence(n, permutation):
    if n == 0:
        return []
    
    dp_dec = [1] * n
    prev = [-1] * n 

    for i in range(1, n):
        for j in range(0, i):
            if permutation[j] > permutation[i]:
                if dp_dec[j] + 1 > dp_dec[i]:
                    dp_dec[i] = dp_dec[j] + 1
                    prev[i] = j

    max_len_dec = max(dp_dec)
    
    lds = []
    idx = dp_dec.index(max_len_dec)
    while idx != -1:
        lds.append(permutation[idx])
        idx = prev[idx]

    lds.reverse()
    return lds


lis = longest_increasing_subsequence(n, numbers)
lds = longest_decreasing_subsequence(n, numbers)

print(' '.join(map(str, lis)))
print(' '.join(map(str, lds)))
