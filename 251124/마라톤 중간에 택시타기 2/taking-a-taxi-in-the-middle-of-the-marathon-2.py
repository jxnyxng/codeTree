n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# 주어진 두번째 체크포인트부터 N-1번째 중 하나씩 빼고 계산
# 계산 결과가 최소인 것만 저장 후 진행

ndist = float('inf')

# 거리계산 함수
def calc(x, y, x2, y2): 
    temp = abs(x-x2) + abs(y-y2)
    return temp

# 메인
for j in range(1, n-1):
    temp = 0
    nx = x[0]
    ny = y[0] 
    for i in range(0, n):
        if i!=j:
            ex = nx
            ey = ny
            nx = x[i]
            ny = y[i]
            temp += calc(ex, ey, nx,ny) #이전 좌표와 현재좌표
    
    ndist = min(ndist, temp)

print(ndist)

