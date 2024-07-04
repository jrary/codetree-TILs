import sys
N1, N2 = map(int, sys.stdin.readline().split())
S1 = set(map(int, sys.stdin.readline().split()))
S2 = set(map(int, sys.stdin.readline().split()))

count = 0

for s in S2:
    if s not in S1:
        count += 1

for s in S1:
    if s not in S2:
        count += 1

print(count)