N = int(input())
arr = [int(input()) for _ in range(N)]

# 배열개수 한개 늘리고 다음 거 체크
# 현재 부호와 다음 부호가 다르면 ans 저장할지 말지 결정
# 같으면 카운트하며 진행

cnt = 1
arr.append(0) # 0은 주어지지 않으므로
ans = 0

for i in range(0, N+1):
    check = (arr[i]>0 and arr[i+1]>0) or (arr[i]<0 and arr[i+1]<0)
    
    if check:
        cnt+=1
    else:
        ans = max(ans, cnt)
        cnt=1

print(ans)