datafile = "../rosalind_data/rosalind_seto.txt"

with open(datafile, 'r') as file:
    lines = file.readlines()
    n = int(lines[0].strip())
    A = list(map(int, lines[1].strip()[1:-1].split(', ')))
    B = list(map(int, lines[2].strip()[1:-1].split(', ')))


def compute_set_operations(n, A, B):
    set_A = set(A)
    set_B = set(B)
    
    union_AB = set_A | set_B  # Union
    intersection_AB = set_A & set_B  # Intersection
    difference_A_B = set_A - set_B  # A - B
    difference_B_A = set_B - set_A  # B - A
    complement_A = set(range(1, n + 1)) - set_A  # A complement
    complement_B = set(range(1, n + 1)) - set_B  # B complement
    
    union_AB = sorted(list(union_AB))
    intersection_AB = sorted(list(intersection_AB))
    difference_A_B = sorted(list(difference_A_B))
    difference_B_A = sorted(list(difference_B_A))
    complement_A = sorted(list(complement_A))
    complement_B = sorted(list(complement_B))
    
    return union_AB, intersection_AB, difference_A_B, difference_B_A, complement_A, complement_B

results = compute_set_operations(n, A, B)
for result in results:
    print("{" + ', '.join(map(str, result)) + "}")
