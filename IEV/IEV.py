datafile = "../rosalind_data/rosalind_iev.txt"

with open(datafile, 'r') as file:
    data = file.read().strip()
    data = list(map(int, data.split()))

# вероятности по каждому фенотипу
probabilities = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]    
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
    
    
expected_offspring = [ data[i] * 2 * probabilities[i] for i in range(len(data)) ]    
total_expected_dominant = sum(expected_offspring)


print(total_expected_dominant)