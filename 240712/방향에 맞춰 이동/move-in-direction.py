import sys
N = int(sys.stdin.readline())
move = []

d = [
    [1, 0],
    [0, -1],
    [-1, 0],
    [0, 1]
]
x, y = 0, 0
for _ in range(N):
    direction, distance = map(str, sys.stdin.readline().split())
    distance = int(distance)
    now_dir = -1
    if direction == 'E':
        now_dir = 0
    elif direction == 'S':
        now_dir = 1
    elif direction == 'W':
        now_dir = 2
    else:
        now_dir = 3
    
    x += d[now_dir][0] * distance
    y += d[now_dir][1] * distance

print(x, y)