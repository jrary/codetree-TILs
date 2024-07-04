import sys
N1 = int(sys.stdin.readline())
s1 = set(map(int, sys.stdin.readline().split()))
N2 = int(sys.stdin.readline())
s2 = list(map(int, sys.stdin.readline().split()))

for num in s2:
    
    print(1 if num in s1 else 0, end = ' ')