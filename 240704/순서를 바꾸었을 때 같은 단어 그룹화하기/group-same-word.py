import sys
N = int(sys.stdin.readline())
li = dict()
for _ in range(N):
    word_list = list(sys.stdin.readline().strip())
    word_list.sort()
    word = ''.join(word_list)
    if word in li:
        li[word] += 1
    else:
        li[word] = 1
res = 0
for k, v in li.items():
    if v > res:
        res = v
print(res)