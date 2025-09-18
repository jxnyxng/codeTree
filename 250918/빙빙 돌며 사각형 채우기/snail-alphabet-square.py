n, m = map(int, input().split())

# 우 하 좌 상 순서로
dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

arr = [[''] * m for _ in range(n)]

# 범위 체크
def in_range(i, j):
    return not(0<=i<n and 0<=j<m)

ni, nj = 0, 0
ndir = 0 
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(n*m):
    if in_range(ni, nj) or arr[ni][nj]!='':
        ni -= di[ndir]
        nj -= dj[ndir]
        ndir = (ndir+1)%4
        ni += di[ndir]
        nj += dj[ndir]

    arr[ni][nj] = alp[i%26]
    ni += di[ndir]
    nj += dj[ndir]
    
        
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()