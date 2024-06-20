## F_n = F_n-1 + k*F_n-2

## n = 5,  k = 3
## month   1   2   3       4       5
## pairs   1   1   1+3*1   1*3+4   4*3+7

n, k = list(map(int, input().split()))
prev, curr  = 1, 1

for _ in range(n-2):
    prev, curr = curr, curr + prev*k

print(curr)