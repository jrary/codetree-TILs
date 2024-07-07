import sys
N, M = map(int, sys.stdin.readline().split())
spot = []
for _ in range(N):
    spot.append(list(map(int, sys.stdin.readline().split())))

spot_comb = []

def select_spot(n, now_spot_comb):
    for i in range(n + 1, N):
        if i not in now_spot_comb:
            new_comb = now_spot_comb + [i]
            if len(new_comb) == M:
                spot_comb.append(new_comb)
            else:
                select_spot(i, new_comb)

length_comb = []

def calc_length(n, now_length_comb):
    for i in range(n + 1, M):
        if i not in now_length_comb:
            new_comb = now_length_comb + [i]
            if len(new_comb) == 2:
                length_comb.append(new_comb)
            else:
                calc_length(i, new_comb)

select_spot(-1, [])
calc_length(-1, [])

min_length = 10000
for spots in spot_comb:
    now_max_length = 0
    for lenspots in length_comb:
        x1, y1 = spot[spots[lenspots[0]]]
        x2, y2 = spot[spots[lenspots[1]]]
        length = (x1 - x2)**2 + (y1 - y2)**2 
        if length > now_max_length:
            now_max_length = length
    if now_max_length < min_length:
        min_length = now_max_length
        
print(min_length)