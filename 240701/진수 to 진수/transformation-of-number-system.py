import sys
from collections import deque
A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

def toDigit (f, n):
    num = n
    li = deque()
    result = 0
    while num > 1:
        li.append(num % 10)
        num //= 10
        if num == 1:
            li.append(num)
            break
    for i in range(len(li)):
        result += li[i] * (f ** i)
    return result

def fromDigit(f, n):
    num = n
    li = deque()
    result = 0
    while num > 1:
        li.appendleft(num % f)
        num //= f
        if num == 1:
            li.appendleft(num)
            break
    for i in range(len(li)):
        result += li[i] * (10 ** i)
    return result

print(fromDigit(B, toDigit(A, N)))