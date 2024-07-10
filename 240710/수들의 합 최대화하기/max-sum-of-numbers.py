import sys
N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

max_sum = 0
def bf(w, h, now_li):
    global max_sum
    for height in range(N):
        if height not in h:
            for width in range(N):
                if width not in w:
                    now_li.append(matrix[width][height])
                    h.append(height)
                    w.append(width)

                    if len(now_li) == N:
                        now_sum = sum(now_li)
                        if now_sum > max_sum:
                            max_sum = now_sum
                    else:
                        bf(w, h, now_li)
                    
                    h.pop()
                    w.pop()
                    now_li.pop()
bf([], [], [])
print(max_sum)