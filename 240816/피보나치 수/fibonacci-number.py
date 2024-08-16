import sys
N = int(sys.stdin.readline())
fibo = []
fibo.append(1)
fibo.append(1)
def dp():
    for i in range(N):
        fibo.append(fibo[i] + fibo[i+1])

dp()
print(fibo[N-1])