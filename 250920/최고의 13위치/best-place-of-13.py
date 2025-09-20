n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n-2): #시작지점 체크 
        cnt=0
        for k in range(3):
            cnt += grid[i][j+k]
        ans = max(ans, cnt)

print(ans)