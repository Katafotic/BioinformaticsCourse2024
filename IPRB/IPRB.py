datafile = "../rosalind_data/rosalind_iprb.txt"

with open(datafile, 'r') as file:
    data = file.read().strip()

k, m, n = list(map(int, data.split()))    

N = k + m + n    
total_pairs = N * (N - 1) / 2
    
kk_pairs = k * (k - 1) / 2
km_pairs = k * m
kn_pairs = k * n
mm_pairs = m * (m - 1) / 2
mn_pairs = m * n
nn_pairs = n * (n - 1) / 2
    
prob_dominant = (kk_pairs * 1.0 + 
                 km_pairs * 1.0 + 
                 kn_pairs * 1.0 + 
                 mm_pairs * 0.75 + 
                 mn_pairs * 0.5 + 
                 nn_pairs * 0.0) / total_pairs
    
print(prob_dominant)