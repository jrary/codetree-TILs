import sys
N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

d = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

def find(x, y):
    now_res = 0
    for dx, dy in d:
        nx = x+dx
        ny = y+dy
        if nx < N and nx >= 0 and ny < N and ny >= 0 and li[nx][ny] == 1:
            now_res += 1
    return now_res

result = 0
for i in range(N):
    for j in range(N):
        now_res = find(i, j)
        if now_res >= 3:
            result += 1

print(result)