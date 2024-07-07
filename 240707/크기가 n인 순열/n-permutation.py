import sys
N = int(sys.stdin.readline())

def bt(now_list):
    for i in range(1, N+1):
        if i not in now_list:
            now_list.append(i)
            if len(now_list) == N:
                print(' '.join(map(str, now_list)))
            else:
                bt(now_list)
            now_list.pop()

bt([])