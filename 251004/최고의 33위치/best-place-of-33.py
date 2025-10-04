n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# N*N 중 M*M -> 가능한 모든 박스 경우

# 1몇갠지 세기
def sol(a, b):
    check = 0
    for i in range(a, a+3):
        for j in range(b, b+3):
            if grid[i][j]==1:
                check+=1
    
    return check
ans=0
# 시작 위치 지정
for i in range(n-2):
    for j in range(n-2):
        ans = max(ans, sol(i, j))

print(ans)

