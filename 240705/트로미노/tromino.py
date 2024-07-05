import sys
N, M = map(int, sys.stdin.readline().split())
tile = []
for _ in range(N):
    tile.append(list(map(int, sys.stdin.readline().split())))
block = [
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 0]],
    [[0, 1], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 2]],
    [[0, 0], [1, 0], [2, 0]]
]

def calc(x, y, block_n):
    now_s = 0
    for i in range(3):
        if (x + block[block_n][i][0] >= N) or (y + block[block_n][i][1] >= M):
            return 0
        now_s += tile[x + block[block_n][i][0]][y + block[block_n][i][1]]
    return now_s

res = 0
for i in range(N):
    for j in range(M):
        for n in range(6):
            now_res = calc(i, j, n)
            if now_res > res:
                res = now_res

print(res)