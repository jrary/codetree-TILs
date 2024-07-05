import sys
input = sys.stdin.read
K, N = map(int, input().split())
now = []

def bt():
    if len(now) == N:
        print(' '.join(map(str, now)))
        return
    for i in range(1, K + 1):
        now.append(i)
        bt()
        now.pop()

bt()