import sys
N, M = map(int, sys.stdin.readline().split())

d = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
res = [[0 for _ in range(M)] for _ in range(N)]
di = 0
x, y = 0, 0
for i in range(1, N*M+1):
    res[x][y] = i
    nx = x + d[di][0]
    ny = y + d[di][1]
    if nx >= M or ny >= N or nx < 0 or ny < 0 or res[nx][ny] != 0:
        di += 1
        if di >= 4:
            di -= 4
    x += d[di][0]
    y += d[di][1]

for li in res:
    print(' '.join(map(str, li)))