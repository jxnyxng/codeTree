n = int(input())
grid = [[0] * n for _ in range(n)]

# 우하단에서 시작, n*n -> 1로 가는 로직과 동일함
# 방향은 좌 상 우 하
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
ndir = 0

def in_range(i, j):
    return not(0<=i<n and 0<=j<n)

ni, nj = n-1, n-1
for i in range(n*n, 0, -1):
    if in_range(ni, nj) or grid[ni][nj]!=0:
        ni -= di[ndir]
        nj -= dj[ndir]
        ndir = (ndir+1)%4
        ni += di[ndir]
        nj += dj[ndir]
    
    grid[ni][nj] = i
    ni += di[ndir]
    nj += dj[ndir]

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()


        



    

