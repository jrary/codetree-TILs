import sys
N = int(sys.stdin.readline())
p = []
for _ in range(N):
    p.append(list(map(int, sys.stdin.readline().split())))

di = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
visited = [[0 for _ in range(N)] for _ in range(N)]
def dfs(a, b):
    count = 1
    visited[a][b] = 1
    for dx, dy in di:
        nx = a + dx
        ny = b + dy
        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == 0 and p[nx][ny] == 1:
            count += dfs(nx, ny)
    return count
    
result = []
for i in range(N):
    for j in range(N):
        if p[i][j] == 1 and visited[i][j] == 0:
            result.append(dfs(i, j))

result.sort()
print(len(result))
for res in result:
    print(res)