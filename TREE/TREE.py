datafile = "../rosalind_data/rosalind_tree.txt"

edges = []
with open(datafile, 'r') as file:
    n = int(file.readline().strip())    
    for line in file:
        u, v = map(int, line.strip().split())
        edges.append((u, v))


def min_edges_to_tree(n, edges):
    from collections import defaultdict
    
    adjacency_list = defaultdict(list)
    
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    visited = [False] * (n + 1)
    components = 0
    
    def dfs(node):
        stack = [node]
        while stack:
            u = stack.pop()
            for v in adjacency_list[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
    
    for i in range(1, n + 1):
        if not visited[i]:
            components += 1
            visited[i] = True
            dfs(i)
    
    return components - 1

print(min_edges_to_tree(n, edges))
