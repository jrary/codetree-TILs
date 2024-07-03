import sys
N, K = map(int, sys.stdin.readline().split())
line = list(0 for _ in range(N))

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b+1):
        line[i-1] += 1

print(max(line))