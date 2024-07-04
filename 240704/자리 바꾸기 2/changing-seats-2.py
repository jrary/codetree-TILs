import sys
N, K = map(int, sys.stdin.readline().split())
now = [i for i in range(N + 1)]
seat = [{i} for i in range(N + 1)]
change = []
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    change.append([a, b])

for j in range(3):
    for a, b in change:
        now[a], now[b] = now[b], now[a]
        seat[now[a]].add(a)
        seat[now[b]].add(b)

for i in range(len(seat) - 1):
    print(len(seat[i + 1]))