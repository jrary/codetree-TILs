import sys
N, M = map(int, sys.stdin.readline().split())

comb = []
def bt(n):
    for i in range(n, N+1):
        if i in comb:
            continue
        comb.append(i)
        if len(comb) == M:
            print(' '.join(map(str, comb)))
        else:
            bt(i)
        comb.pop()

bt(1)