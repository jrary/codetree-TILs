import sys
N, M = map(int, sys.stdin.readline().split())
route = []
for _ in range(N):
    route.append(list(map(int, sys.stdin.readline().split())))
d = [
    [0, 1],
    [1, 0]
]

def dfs(a, b):
    if a == N-1 and b == M-1:
        return 1
    for i in range(2):
        na = a + d[i][0]
        nb = b + d[i][1]
        if na < N and nb < M and route[na][nb] == 1:
            return dfs(na, nb)

print(1 if dfs(0, 0) else 0)