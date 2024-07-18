import sys
N, M = map(int, sys.stdin.readline().split())
node = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    node[x][y] = 1
    node[y][x] = 1

stack = [1]
visited = [0 for _ in range(N + 1)]
res = 0
visited[1] = 1
while stack:
    now = stack.pop()
    for i in range(1, N+1):
        if node[now][i] == 1 and visited[i] != 1:
            visited[i] = 1
            stack.append(i)
            res += 1

print(res)