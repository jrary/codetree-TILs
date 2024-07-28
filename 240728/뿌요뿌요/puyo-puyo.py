import sys
N = int(sys.stdin.readline())
block = []
for _ in range(N):
    block.append(list(map(int, sys.stdin.readline().split())))

di = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
visited = [[0 for _ in range(N)] for _ in range(N)]
def dfs(a, b, k):
    count = 1
    visited[a][b] = 1
    for dx, dy in di:
        nx = a + dx
        ny = b + dy
        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == 0 and block[nx][ny] == k:
            count += dfs(nx, ny, k)
    return count

result = []
count = 0
for k in range(100):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and block[i][j] == k:
                res = dfs(i, j, k)
                result.append(res)
                if res >= 4:
                    count += 1

print(count, max(result))