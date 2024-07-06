import sys
from collections import deque
N = int(sys.stdin.readline())
N_li = deque()
n = N
while n > 0:
    N_li.appendleft(n % 10)
    n //= 10

def bt():
    while first:
        count = 1
        for i in range(1, N_li[k]):
            if N_li[first] == N_li[first + i]:
                count += 1
        if count == N_li[k]:
            first += N_li[k]
        else:
            return False

print(N_li)