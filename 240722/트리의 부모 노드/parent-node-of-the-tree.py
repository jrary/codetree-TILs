import sys
N = int(sys.stdin.readline())
node = []
node.append([0, 0])
node.append([0, 0])
for _ in range(N):
    node.append(list(map(int, sys.stdin.readline().split())))
visited = [0 for _ in range(N+1)]

for i in range(2, N+1):
    if visited[i] == 0:
        visited[i] = node[i][0]
    else:
        visited[i] = visited[visited[i]]

for i in range(2, N+1):
    print(visited[i])