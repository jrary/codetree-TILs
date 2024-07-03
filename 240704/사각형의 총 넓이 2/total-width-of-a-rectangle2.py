import sys
N = int(sys.stdin.readline())
rect = []
min_x = 0
min_y = 0
max_x = 0
max_y = 0
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a < min_x:
        min_x = a
    if b < min_y:
        min_y = b
    if c > max_x:
        max_x = c
    if d > max_y:
        max_y = d
    rect.append([a, b, c, d])

for i in range(N):
    rect[i][0] -= min_x
    rect[i][1] -= min_y
    rect[i][2] -= min_x
    rect[i][3] -= min_y

coo = [[0 for _ in range(max_y - min_y)]for _ in range(max_x - min_x)]
print(rect)
print(coo)
for a, b, c, d in rect:
    for i in range(a, c):
        for j in (b, d):
            print(i, j)
            coo[i][j] = 1

print(coo.count(1))