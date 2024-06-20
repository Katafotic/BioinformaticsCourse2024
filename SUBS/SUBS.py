import sys

seq, reference = map(str.rstrip, sys.stdin.readlines())

positions = []
for pos in range(len(seq)):
    if seq[pos:].startswith(reference):
        positions.append(pos + 1)

print(*positions)