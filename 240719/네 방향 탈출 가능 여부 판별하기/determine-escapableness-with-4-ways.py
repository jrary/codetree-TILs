import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
snake = []
for _ in range(N):
    snake.append(list(map(int, sys.stdin.readline().split())))
di = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

visited = [[0 for _ in range(M)] for _ in range(N)]
def bfs():
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.pop()
        visited[x][y] = 1
        if x == N - 1 and y == M - 1:
            return 1
        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0 and snake[nx][ny] == 1:
                queue.append([nx, ny])


print(1 if bfs() else 0)