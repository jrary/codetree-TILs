import sys
rect = []
min_x = 1000
min_y = 1000
max_x = -1000
max_y = -1000
for _ in range(2):
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

for i in range(2):
    for j in range(2):
        rect[i][j * 2] -= min_x
        rect[i][j * 2 + 1] -= min_y

# -1이 없는 상태, 0이 표시된 상태, 1이 지워진 상태
coo = [[-1 for _ in range(max_y - min_y)] for _ in range(max_x - min_x)]
for k in range(2):
    for i in range(rect[k][0], rect[k][2]):
        for j in range(rect[k][1], rect[k][3]):
            coo[i][j] = k

len_x = len(coo)
len_y = len(coo[0])
min_rx = -1
min_ry = -1
max_rx = min_x
max_ry = min_y

for i in range(len_x):
    for j in range(len_y):
        if coo[i][j] == 0:
            if min_rx == -1 and min_ry == -1:
                min_rx = i
                min_ry = j
                continue
            else:
                if i > max_rx:
                    max_rx = i
                if j > max_ry:
                    max_ry = j

print((max_rx - min_rx + 1) * (max_ry - min_ry + 1))