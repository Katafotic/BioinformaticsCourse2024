datafile = "../rosalind_data/rosalind_inod.txt"

with open(datafile, 'r') as file:
    n = int(file.readline().strip())

## Hint:
## In solving “Completing a Tree”, you may have formed the conjecture that a graph with no cycles and n nodes is a tree precisely when it has n−1 edges. This is indeed a theorem of graph theory.
print(n-2)
