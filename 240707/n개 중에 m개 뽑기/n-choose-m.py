import sys
N, M = map(int, sys.stdin.readline().split())

def bt(comb):
    if len(comb) == M:
        print(comb)
    for i in range(1, N+1):
        if i in comb:
            continue
        bt(comb.append(i))

bt([])