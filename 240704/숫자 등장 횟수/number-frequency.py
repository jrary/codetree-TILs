import sys
N, M = map(int, sys.stdin.readline().split())
li = dict()
inp = list(map(int, sys.stdin.readline().split()))
for i in inp:
    if i in li:
        li[i] += 1
    else:
        li[i] = 1

res_in = list(map(int, sys.stdin.readline().split()))
for i in range(len(res_in)):
     if res_in[i] not in li:
        li[res_in[i]] = 0

for r in res_in:
    print(li[r], end=' ')