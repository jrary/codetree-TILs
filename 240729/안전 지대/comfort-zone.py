import sys
N, M = map(int, sys.stdin.readline().split())
v = []
max_v = 0
min_v = 100
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    v.append(line)

    now_max = max(line)
    now_min = min(line)
    if now_max > max_v:
        max_v = now_max
    if now_min < min_v:
        min_v = now_min

di = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]
visited = [[0 for _ in range(M)] for _ in range(N)]
def dfs(k, x, y):
    visited[x][y] = 1
    for dx, dy in di:
        nx = x + dx
        ny = y + dy
        if nx < N and ny < M and nx >= 0 and ny >= 0 and visited[nx][ny] == 0 and v[nx][ny] > k:
            dfs(k, nx, ny)

max_cnt = 0
max_k = min_v
for k in range(min_v, max_v + 1):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    now_count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and v[i][j] > k:
                now_count += 1
                dfs(k, i, j)
    if now_count > max_cnt:
        max_cnt = now_count
        max_k = k

print(max_k, max_cnt)