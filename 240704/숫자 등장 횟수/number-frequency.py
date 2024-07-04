import sys
N, M = map(float, sys.stdin.readline().split())
li = dict()
inp = list(map(float, sys.stdin.readline().split()))
for i in inp:
    if i in li:
        li[i] += 1
    else:
        li[i] = 1
a, b = map(float, sys.stdin.readline().split())
if a not in li:
    li[a] = 0
if b not in li:
    li[b] = 0
print(li[a], li[b])