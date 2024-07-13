import sys
move = list(sys.stdin.readline().strip())

d = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

di = 0
x = 0
y = 0
for m in move:
    if m == 'L':
        di -= 1
        if di < 0:
            di += 4
    elif m == 'R':
        di += 1
        if di > 3:
            di -= 4
    elif m == 'F':
        x += d[di][0]
        y += d[di][1]

print(x, y)