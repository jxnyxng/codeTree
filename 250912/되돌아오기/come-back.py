N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0

drs = {'N':0, 'S':1, 'E':2, 'W':3}
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

time = 0
for i in range(N): 
    ndir_idx = drs[dir[i]]
    ndist = dist[i]

    for j in range(ndist):
        time+=1
        x = x+dx[ndir_idx]
        y = y+dy[ndir_idx]
        if x==0 and y==0: 
            break
    
    if x==0 and y==0: 
        break

if x!=0 or y!=0:
    print(-1)
else:
    print(time)



        