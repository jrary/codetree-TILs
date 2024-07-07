import sys
N = int(sys.stdin.readline())
line = []
for _ in range(N):
    line.append(list(map(int, sys.stdin.readline().split())))

res = 0
def bt(end):
    global res
    min_end = 1001
    for f, e in line:
        if f > end:
            if e < min_end:
                min_end = e
    if min_end > 1000:
        return
    else:
        res += 1
        bt(min_end)

bt(0)
print(res)