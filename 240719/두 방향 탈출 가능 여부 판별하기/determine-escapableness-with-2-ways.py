import sys
sys.setrecursionlimit(10000)  # 재귀 한도를 늘립니다.

N, M = map(int, sys.stdin.readline().split())
route = []
for _ in range(N):
    route.append(list(map(int, sys.stdin.readline().split())))

d = [
    [0, 1],
    [1, 0]
]

def dfs(a, b, visited):
    if a == N-1 and b == M-1:
        return True
    visited[a][b] = True
    for i in range(2):
        na = a + d[i][0]
        nb = b + d[i][1]
        if 0 <= na < N and 0 <= nb < M and route[na][nb] == 1 and not visited[na][nb]:
            if dfs(na, nb, visited):
                return True
    visited[a][b] = False  # 탐색을 위해 다시 False로 바꿉니다.
    return False

visited = [[False] * M for _ in range(N)]
print(1 if dfs(0, 0, visited) else 0)