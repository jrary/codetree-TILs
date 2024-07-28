import sys
from collections import defaultdict, deque

def bfs(start, n, adj_list):
    distances = [-1] * (n + 1)
    distances[start] = 0
    q = deque([start])
    
    farthest_node = start
    max_distance = 0
    
    while q:
        current = q.popleft()
        for neighbor, weight in adj_list[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + weight
                q.append(neighbor)
                if distances[neighbor] > max_distance:
                    max_distance = distances[neighbor]
                    farthest_node = neighbor
                    
    return farthest_node, max_distance

def find_tree_diameter(n, edges):
    adj_list = defaultdict(list)
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    farthest_node, _ = bfs(1, n, adj_list)
    
    _, diameter = bfs(farthest_node, n, adj_list)
    
    return diameter

input = sys.stdin.read
data = input().split()
n = int(data[0])
edges = []
index = 1
for _ in range(n - 1):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    edges.append((u, v, w))
    index += 3

diameter = find_tree_diameter(n, edges)
print(diameter)