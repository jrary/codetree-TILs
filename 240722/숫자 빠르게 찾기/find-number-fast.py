import sys
N, M = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

def bs(m):
    idx = -1
    left, right = 0, N-1
    while left <= right:
        mid = (left+right) // 2
        if number[mid] == m:
            idx = mid + 1
            break
        elif number[mid] > m:
            right = mid - 1
        else:
            left = mid + 1
    return idx

for _ in range(M):
    m = int(sys.stdin.readline())
    print(bs(m))