n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 인접한 위치 1이 3개 이상인 곳
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n  and 0 <= y and y < n

ans=0

for i in range(n):
    for j in range(n):
        cnt=0
        for ndx, ndy in zip(dx, dy):
            nx = i+ndx
            ny = j+ndy
            if in_range(nx,ny) and grid[nx][ny]:
                cnt+=1
        if cnt>=3:
            ans+=1

print(ans)

                


