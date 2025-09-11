n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)] 

# 하 우 상 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

x, y = 0, 0
arr[x][y] = 1 
dir_n = 0

for i in range(2, n * m + 1):
    nx, ny = x + dx[dir_n], y + dy[dir_n]
    
    # 범위를 벗어낫거나 이미 방문햇을때
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_n = (dir_n + 1) % 4 # 방향
        nx, ny = x + dx[dir_n], y + dy[dir_n]
    
    x, y = nx, ny
    arr[x][y] = i

for i in arr:
    for j in i:
        print(j,end=' ')
    print()
