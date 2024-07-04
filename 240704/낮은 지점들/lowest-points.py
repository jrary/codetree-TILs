import sys
N = int(sys.stdin.readline())
li = dict()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x in li:
        if y < li[x]:
            li[x] = y
    else:
        li[x] = y

res = 0
for x, y in li.items():
    res += y

print(res)