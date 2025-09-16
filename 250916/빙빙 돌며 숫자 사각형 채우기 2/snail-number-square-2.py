n, m = map(int, input().split())

# 0,0 에서 시작해 아래 오른 위 왼 반복
# 벽 만나거나 이미 방문한곳 만나면 방향 바꿔서 전진

arr = [[0] * m for _ in range(n)]

# 하 우 상 좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 범위 체크
def in_range(i, j):
    return not(0<=i<n and 0<=j<m)

ni, nj = 0, 0
ndir = 0

for i in range((n*m)):
    if in_range(ni, nj) or arr[ni][nj]!=0:
        ni -= di[ndir]
        nj -= dj[ndir]
        ndir = (ndir+1)%4
        ni += di[ndir]
        nj += dj[ndir]
    

    arr[ni][nj] = (i+1)
    ni += di[ndir]
    nj += dj[ndir]


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()



