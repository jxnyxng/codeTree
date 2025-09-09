n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx = [1, -1 , 0, 0]
dy = [0, 0, -1, 1]

x = 0
y = 0

for i in range(n):
    if dir[i]=='E':
        idx = 0
    elif dir[i]=='W':
        idx = 1
    elif dir[i]=='S':
        idx = 2
    elif dir[i]=='N':
        idx = 3

    x += (dx[idx]*dist[i])
    y += (dy[idx]*dist[i])
print(x, y)