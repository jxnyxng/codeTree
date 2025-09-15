n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# 주어진 위치를 색칠
# 상하좌우가 범위 내의 색칠된 칸인지 체크
# 3개가 맞으면 카운트

# 1~n
arr = [[0] * (n+1) for _ in range(n+1)]
# 상하좌우
dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]
# 범위 체크 함수
def in_range(i, j):
    return 1<=i<=n and 1<=j<=n

def is_colored(i, j):
    if arr[i][j] == 1:
        return 1
    else:
        return 0

# 색칠 시작
for p in range(m):
    ni = points[p][0]
    nj = points[p][1]
    cnt = 0
    arr[ni][nj] = 1

    for i in range(4):
        cni = ni + dxs[i]
        cnj = nj + dys[i]

        if in_range(cni, cnj):
            cnt += is_colored(cni, cnj)
    if cnt==3:
        print(1)
    else:
        print(0)

        


    
