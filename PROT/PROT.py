from Bio.Seq import Seq

seq = Seq(input().rstrip())
protein = seq.translate().rstrip("*")
print(protein)

