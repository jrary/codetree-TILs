import sys
from collections import deque
N, K, U, D = map(int, sys.stdin.readline().split())
building = []
for _ in range(N):
    building.append(list(map(int, sys.stdin.readline().split())))
di = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

visited = [[0 for _ in range(N)] for _ in range(N)]
def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    count = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        count += 1
        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == 0:
                height_abs = abs(building[x][y] - building[nx][ny])
                if height_abs >= U and height_abs <= D:
                    queue.append([nx, ny])
    return count

result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            result.append(bfs(i, j))

result.sort(reverse=True)
res = 0
for i in range(K):
    res += result[i]

print(res)