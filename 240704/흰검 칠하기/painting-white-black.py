import sys
N = int(sys.stdin.readline())
check = []
min_front = 0
max_back = 0
for _ in range(N):
    x, y = map(str, sys.stdin.readline().split())
    x = int(x)
    if y == 'R':
        max_back += x
    elif y == 'L':
        min_front += x
    check.append([x, y])
# 검은색: 0, 흰색: 1
tile = list([] for _ in range(min_front + max_back + 1))
pt = min_front
for x, y in check:
    if y == 'R':
        for i in range(x):
            tile[pt + i].append(0)
        pt += (x - 1)
    elif y == 'L':
        for i in range(x):
            tile[pt - i].append(1)
        pt -= (x - 1)

white = 0
gray = 0
black = 0
for arr in tile:
    if len(arr) < 1:
        continue
    elif arr.count(0) >= 2 and arr.count(1) >= 2:
        gray += 1
    elif arr[-1] == 0:
        black += 1
    else:
        white += 1
        
print(white, black, gray)