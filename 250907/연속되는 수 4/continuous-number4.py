n = int(input())
arr = [int(input()) for _ in range(n)]

# 다음 값이 현재값보다 작을때 카운트 종료
# -> 카운트하며 저장해둔 배열 길이로 비교하여 긴 거 저장

arr.append(0)
ans = 0
cnt = 1

for i in range(n):
    if arr[i] >= arr[i+1]:
        ans = max(ans, cnt)
        cnt=1
    else:
        cnt+=1

print(ans)

    
