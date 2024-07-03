import sys
blue_rect = []
for _ in range(2):
    blue_rect.append(list(map(int, sys.stdin.readline().split())))
rx1, ry1, rx2, ry2 = map(int, sys.stdin.readline().split())

min_x = min(blue_rect[0][0], blue_rect[1][0], rx1) if min(blue_rect[0][0], blue_rect[1][0], rx1) < 0 else 0
min_y = min(blue_rect[0][1], blue_rect[1][1], ry1) if min(blue_rect[0][1], blue_rect[1][1], ry1) < 0 else 0
max_x = max(blue_rect[0][2], blue_rect[1][2], rx2) 
max_y = max(blue_rect[0][3], blue_rect[1][3], ry2) 

for i in range(2):
    blue_rect[i][0] -= min_x
    blue_rect[i][1] -= min_y
    blue_rect[i][2] -= min_x
    blue_rect[i][3] -= min_y

rx1 -= min_x
ry1 -= min_y
rx2 -= min_x
ry2 -= min_y

coo = [[0 for _ in range(max_y - min_y)] for _ in range(max_x - min_x)]
for x1, y1, x2, y2 in blue_rect:
    for i in range(x1, x2):
        for j in range(y1, y2):
            coo[i - 1][j - 1] = 1

for i in range(rx1, rx2):
    for j in range(ry1, ry2):
        coo[i - 1][j - 1] = 0

res = 0
for arr in coo:
    res += arr.count(1)

print(res)