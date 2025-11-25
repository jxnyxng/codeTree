n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans=0
# 케이스 1 : 서로 다른 행에 위치한 두 격자인 경우
for i in range(n-1):
    for j in range(n-2):
        # 첫번째 범위 탐색
        first=0
        for k in range(j, j+3):
            if arr[i][k]==1:
                first+=1
        for x in range(i+1, n):
            for v in range(0, n-2):
                second=0
                for k in range(v, v+3):
                    if arr[x][k]==1:
                        second+=1
                ans = max(ans, (first+second))
 
# 케이스 2 : 같은 행에 위치한 두격자를 고른 경우
ans1=0
if n>=6:
    for i in range(n):
            for j in range(n-5):
                first=0
                # 첫번째 간격 설정
                for k in range(j, j+3):
                    if arr[i][k]==1:
                        first+=1
                # 두번째 간격 설정
                for k in range(j+3, n-2):
                    second=0
                    for x2 in range(k,k+3): 
                        if arr[i][x2]==1:
                            second+=1
                    ans1 = max(ans1, first+second)
            
print(max(ans1, ans))
