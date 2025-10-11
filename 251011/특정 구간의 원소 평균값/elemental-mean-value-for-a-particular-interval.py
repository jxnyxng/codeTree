n = int(input())
arr = list(map(int, input().split()))

ans=0
# 시작점
for i in range(n):
    # 끝점
    for j in range(i, n):   
        # 범위 내 평균구하기
        # 있는지 확인 
        med = sum(arr[i:j+1])/(j-i+1)
        if med in arr[i:j+1]: 
            ans+=1

print(ans)