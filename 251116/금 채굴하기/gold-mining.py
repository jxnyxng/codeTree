from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 범위를 벗어나면 종료
# bfs 반복은 마름모 크기에 따라 결정 (가장 작은 마름모 -> bfs 0회)

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

q = deque()
def bfs(i, j, k):
    global ans
    visited = [[False] * n for _ in range(n)] 
    q.append((i,j,k))

    gold_cnt = 0 
    gain = 0
    cost = (k*k) + ((k+1) * (k+1))

    while q:
        nowi, nowj, nowk = q.popleft() 
        # 현재 위치가 금이면 카운트
        if not visited[nowi][nowj] and grid[nowi][nowj] == 1:
            gold_cnt+=1
            gain+=m
         
        visited[nowi][nowj] = True

        # 기회가 있을 때만
        if nowk!=0: 
            for idx in range(4):
                newi, newj = nowi + dys[idx], nowj+dxs[idx] 
                if in_range(newi, newj) and not visited[newi][newj]:
                    q.append((newi,newj,nowk-1))
                 
    if (gain-cost)>=0:
        ans=max(ans, gold_cnt)
    

ans = 0
# 마름모 크기 결정 후 시작점 결정
# k가 n-1 이면 다 덮는다
for k in range(n):
    for i in range(n): 
        for j in range(n):
            bfs(i,j,k) 
print(ans)