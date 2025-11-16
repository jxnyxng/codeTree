from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 범위를 벗어나면 종료
# bfs 반복은 마름모 크기에 따라 결정 (가장 작은 마름모 -> bfs 0회)

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(i,j):
    return 0<=i<n and 0<=j<n
    
def bfs(i, j):
    global ans
    
    q = deque()
    visited = [[False] * n for _ in range(n)] 
    
    q.append((i,j))
    visited[i][j] = True

    gold_cnt = 0  
    k = 0

    while q:
        q_len = len(q)
        
        for _ in range(q_len):
            nowi, nowj = q.popleft()

            if grid[nowi][nowj] == 1:
                gold_cnt += 1
            
            for idx in range(4):
                newi, newj = nowi + dys[idx], nowj + dxs[idx]
                if in_range(newi, newj) and not visited[newi][newj]:
                    visited[newi][newj] = True
                    q.append((newi,newj))
        
        cost = (k*k) + ((k+1) * (k+1))
        gain = gold_cnt * m
             
        if (gain-cost) >= 0:
            ans=max(ans, gold_cnt)
        
        k += 1

ans = 0

for i in range(n): 
    for j in range(n):
        bfs(i,j)

print(ans)