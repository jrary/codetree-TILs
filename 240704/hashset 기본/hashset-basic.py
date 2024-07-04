import sys
N = int(sys.stdin.readline())
s = set()
for _ in range(N):
    order, x = map(str, sys.stdin.readline().split())
    x = int(x)
    
    if order == 'find':
        print('true' if x in s else 'false')
    elif order == 'add':
        s.add(x)
    elif order == 'remove':
        s.remove(x)