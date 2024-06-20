from itertools import product
datafile = "../rosalind_data/rosalind_lexv.txt"

with open(datafile, 'r') as file:
    alphabet = file.readline().split()
    n = int(file.read())

# alphabet = ["D", "N", "A"]
# n = 3

def generate_strings(alphabet, max_length, prefix="", results=None):
    if results is None:
        results = []
    if len(prefix) <= max_length:
        if prefix:
            results.append(prefix)
        if len(prefix) < max_length:
            for char in alphabet:
                generate_strings(alphabet, max_length, prefix + char, results)
    return results

def generate_strings_from_alphabet(alphabet, n):
    alphabet = list(alphabet)
    strings = generate_strings(alphabet, n)
    for s in strings:
        print(s)

generate_strings_from_alphabet(alphabet, n)
