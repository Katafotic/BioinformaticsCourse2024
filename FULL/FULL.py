import random

datafile = "../rosalind_data/rosalind_full.txt"
with open(datafile, "r") as f:
    L = [float(line.strip()) for line in f]
    p, l = L[0], L[1:]

# mass_table = {
#     'A': 71.03711,
#     'C': 103.00919,
#     'D': 115.02694,
#     'E': 129.04259,
#     'F': 147.06841,
#     'G': 57.02146,
#     'H': 137.05891,
#     'I': 113.08406,
#     'K': 128.09496,
#     'L': 113.08406,
#     'M': 131.04049,
#     'N': 114.04293,
#     'P': 97.05276,
#     'Q': 128.05858,
#     'R': 156.10111,
#     'S': 87.03203,
#     'T': 101.04768,
#     'V': 99.06841,
#     'W': 186.07931,
#     'Y': 163.06333
# }

mass_table = {
    71.03711: ["A"],
    103.00919: ["C"],
    115.02694: ["D"],
    129.04259: ["E"],
    147.06841: ["F"],
    57.02146: ["G"],
    137.05891: ["H"],
    128.09496: ["K"],
    113.08406: ["I", "L"],
    131.04049: ["M"],
    114.04293: ["N"],
    97.05276: ["P"],
    128.05858: ["Q"],
    156.10111: ["R"],
    87.03203: ["S"],
    101.04768: ["T"],
    99.06841: ["V"],
    186.07931: ["W"],
    163.06333: ["Y"],
    }


def inferring_peptide(n, p, l, peptide=[""]):

    if len(peptide[0])==n:
        return peptide

    BYions = []
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            aa = mass_table.get(round(l[j]-l[i], 5), 0)
            if aa:
                BYions.append([i, j, aa])
    
    if BYions[0]:        
        new_l = l[BYions[0][1]:]
        new_p = BYions[0][2]
        new_peptide = [p+np for np in new_p for p in peptide]
        peptide =inferring_peptide(n, p, new_l, new_peptide)

    return peptide

n = (len(l) - 2) // 2
t = inferring_peptide(n, p, l)
print("totally {} possible multiple solutions exist.".format(len(t)))
print("randomly select 1 solution:\n{}".format(random.sample(t, k=1)[0]))