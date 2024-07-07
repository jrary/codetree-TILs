import sys
N = int(sys.stdin.readline())

bn = []
res = 0

def bf():
    global res
    for i in range(1, 5):
        for _ in range(i):
            bn.append(i)
        
        if len(bn) == N:
            res += 1
        elif len(bn) < N:
            bf()

        for _ in range(i):
            bn.pop()

bf()
print(res)