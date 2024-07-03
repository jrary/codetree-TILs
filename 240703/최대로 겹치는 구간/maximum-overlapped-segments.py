import sys
N = int(sys.stdin.readline())

check = []
min_start = 0
max_end = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    check.append([a, b])
    if a < min_start:
        min_start = a
    if b > max_end:
        max_end = b

# 모든 좌표에 대해 특정 offset(min_start: 최소숫자)을 더한다.
for i in range(N):
    check[i][0] -= min_start
    check[i][1] -= min_start

line = list(0 for _ in range(max_end - min_start))
for a, b in check:
    for i in range(a, b):
        line[i] += 1

print(max(line))