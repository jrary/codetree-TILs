import sys
from collections import deque
N = int(sys.stdin.readline())
flip = []
# 검은색 0, 흰색 1
card = deque()
pt = 0
for _ in range(N):
    x, Y = map(str, sys.stdin.readline().split())
    X = int(x)
    if Y == 'R':
        if len(card) < X:
            card = deque()
            pt = 0
            for _ in range(X):
                card.appendleft(0)
        elif pt == 0:
            for _ in range(X):
                card.appendleft(0)
        else:
            for i in range(pt, pt-X):
                card[i] = 0
    elif Y == 'L':
        if len(card) < X:
            card = deque()
            pt = X - 1
            for _ in range(X):
                card.append(1)
        elif pt == len(card) - 1:
            for _ in range(X):
                card.append(1)
        else:
            for i in range(pt, pt+X):
                card[i] = 1

print(card.count(1), card.count(0))