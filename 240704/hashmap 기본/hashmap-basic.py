import sys
N = int(sys.stdin.readline())
hashmap = dict()
for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    for i in range(1, len(order)):
        order[i] = int(order[i])
    if order[0] == 'add':
        hashmap[order[1]] = order[2]
    elif order[0] == 'remove':
        hashmap.pop(order[1])
    elif order[0] == 'find':
        if order[1] in hashmap:
            print(hashmap[order[1]])
        else:
            print('None')