import numpy as np

# datafile = "../rosalind_data/rosalind_lgis.txt"

# with open(datafile, 'r') as file:
#     s = file.readline().strip()
#     probability = list(map(float, file.readline().split()))

s = "TGGTTGGCGGTGAGGCCCATCACCCTTCTAAGGACTGTGTGAAACAGAAGATAGCCTCATGCAAGGTTTTGATGTTATATTGGGGAGACTCGATGTCT"
probability = [0.083, 0.117, 0.195, 0.230, 0.271, 0.329, 0.372, 0.450, 0.503, 0.551, 0.630, 0.654, 0.726, 0.757, 0.815, 0.877, 0.933]

def compute_gc_probability(s, x):
    gc_prob = x / 2
    at_prob = (1 - x) / 2
    
    prob = 1.0
    for nucleotide in s:
        if nucleotide in 'GC':
            prob *= gc_prob
        elif nucleotide in 'AT':
            prob *= at_prob
        else:
            raise ValueError(f"Invalid nucleotide found in string s: {nucleotide}")
    
    return prob

def log_probability(s, A):
    B = []
    for x in A:
        prob = compute_gc_probability(s, x)
        log_prob = np.log10(prob)
        B.append(log_prob)
    
    return B

B = log_probability(s, probability)
print(*B)