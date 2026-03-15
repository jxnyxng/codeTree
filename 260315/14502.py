# 백준 14502번
from collections import deque
import copy

# 입력
N, M = map(int, input().split())
graph = []
for _ in range(N):
    l = list(map(int, input().split()))
    graph.append(l)
    
# dx dy
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

# in_range
def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

ans = 0
# bfs
def bfs():
    global ans
    q = deque()
    new_graph = copy.deepcopy(graph)    

    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                q.append((i,j))
    
    while q:
        nowi, nowj = q.popleft()

        for i in range(4):
            ni, nj = nowi + dys[i], nowj + dxs[i]
            
            if not in_range(ni, nj):
                continue

            if new_graph[ni][nj] == 0:
                new_graph[ni][nj] = 2
                q.append((ni, nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 0:
                cnt+=1         
    ans = max(ans, cnt)                

# make wall
def makeWall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(wall_cnt+1)
                graph[i][j] = 0

makeWall(0)
print(ans)                