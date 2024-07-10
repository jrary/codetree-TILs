import sys

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

col_arr = []

def bf(now_li):
    if len(now_li) == N:
        col_arr.append(now_li)
        return
    
    for i in range(N):
        if i not in now_li:
            now_li.append(i)
            bf(now_li)
            now_li.pop()

bf([])

max_sum = 0
for arr in col_arr:
    now_sum = 0
    for i in range(N):
        now_sum += matrix[i][arr[i]]
    if now_sum > max_sum:
        max_sum = now_sum

print(max_sum)