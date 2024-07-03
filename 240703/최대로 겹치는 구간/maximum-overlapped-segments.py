import sys
N = int(sys.stdin.readline())
line = list(0 for _ in range(100))
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b):
        line[i] += 1

print(max(line))