from scipy.stats import binom

datafile = "../rosalind_data/rosalind_lia.txt"

with open(datafile, 'r') as file:
    data = file.read().strip()
    k, N = list(map(int, data.split()))

# Общее количество потомков в k-м поколении
total_offspring = 2**k
    
# Вероятность потомока Aa Bb
p_AaBb = 1 / 4
    
cum_prob = sum(binom.pmf(i, total_offspring, p_AaBb) for i in range(N))
    
# У нас должно быть по крайней мере N Aa Bb особей
prob_at_least_N = 1 - cum_prob

print(prob_at_least_N)
