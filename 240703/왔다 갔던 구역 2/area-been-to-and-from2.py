import sys
N = int(sys.stdin.readline())
move = []
min_front = 0
max_back = 0
for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    move.append([a, b])
    if b == 'L':
        min_front += a
    elif b == 'R':
        max_back += a

# for i in range(N):
#     move[i][0] += min_front

line = list(0 for _ in range(max_back + min_front))
pt = min_front
for a, b in move:
    if b == 'R':
        for i in range(a):
            line[pt + i] += 1
        pt += a
    elif b == 'L':
        for i in range(1, a+1):
            line[pt - i] += 1
        pt -= a
print(len([x for x in line if x > 1]))