import sys
N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

xor = 0
stack = []
def bt(n):
    global xor
    for i in range(n, N+1):
        if i in stack:
            continue
        stack.append(i)
        if len(stack) == M:
            now_xor = 0
            for j in range(M):
                now_xor ^= card[stack[j] - 1]
            if now_xor > xor:
                xor = now_xor
        else:
            bt(i)
        stack.pop()

bt(1)
print(xor)