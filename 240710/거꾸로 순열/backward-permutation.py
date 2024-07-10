import sys
N = int(sys.stdin.readline())

def bf(now_list):
    for i in range(N, 0, -1):
        if i not in now_list:
            now_list.append(i)
            if len(now_list) == N:
                print(' '.join(map(str, now_list)))
            else:
                bf(now_list)
            now_list.pop()

bf([])