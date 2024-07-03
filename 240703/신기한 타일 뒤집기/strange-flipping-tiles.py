import sys
from collections import defaultdict

N = int(sys.stdin.readline())
commands = [sys.stdin.readline().strip() for _ in range(N)]

# 검은색: 0, 흰색: 1
tiles = defaultdict(int)
current_position = 0

for command in commands:
    X, Y = command.split()
    X = int(X)
    
    if Y == 'R':
        for i in range(current_position, current_position + X):
            tiles[i] = 0  
        current_position += X - 1  
    
    elif Y == 'L':
        for i in range(current_position, current_position - X, -1):
            tiles[i] = 1 
        current_position -= X - 1  

white_count = sum(1 for color in tiles.values() if color == 1)
black_count = sum(1 for color in tiles.values() if color == 0)

print(white_count, black_count)