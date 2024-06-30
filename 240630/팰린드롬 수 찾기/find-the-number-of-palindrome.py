import sys
X, Y = map(int, sys.stdin.readline().split())
result = 0

for n in range(X, Y + 1):
    now = n
    now_list = []
    while n >= 1:
        now_list.append(n % 10)
        n //= 10
    for i in range(0, len(now_list) // 2):
        if now_list[i] == now_list[-(i + 1)]:
            if i == len(now_list) // 2 - 1:
                result += 1
        else:
            break

print(result)