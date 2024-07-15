import sys
N = int(sys.stdin.readline())
mirror = []
for _ in range(N):
    mirror.append(list(sys.stdin.readline().strip()))
K = int(sys.stdin.readline())

d = [
    [1, 0],
    [0, -1],
    [-1, 0],
    [0, 1]
]

a = K // N
b = K % N
x, y = 0, 0
di = a
if a == 0:
    x = 0
    y = b - 1
elif a == 1:
    x = b - 1
    y = N - 1
elif a == 2:
    x = N - 1
    y = b - 1
elif a == 3:
    x = N-b
    y = 0

count = 0
while x < N and x >= 0 and y < N and y >= 0:
    count += 1
    if mirror[x][y] == '\\':
        if di == 0:
            di = 3
        elif di == 1:
            di = 2
        elif di == 2:
            di = 1
        elif di == 3:
            di = 0
    elif mirror[x][y] == '/':
        if di == 0:
            di = 1
        elif di == 1:
            di = 0
        elif di == 2:
            di = 3
        elif di == 3:
            di = 2
    x += d[di][0]
    y += d[di][1]

print(count)