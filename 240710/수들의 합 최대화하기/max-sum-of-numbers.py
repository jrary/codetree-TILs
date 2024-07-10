import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
matrix = []
index = 1
for i in range(N):
    matrix.append(list(map(int, data[index:index + N])))
    index += N

col_arr = []

def bf(now_li):
    if len(now_li) == N:
        col_arr.append(now_li[:])
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