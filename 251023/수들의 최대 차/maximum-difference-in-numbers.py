N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
 
# 최대 최소 차이가 k까지 허용 a~a+k
# 소팅하고 좌우에서 k이내에 들어오는 지점이 정답?
arr.sort()
cnt = 0
for i in range(N): 
    for j in range(i, N):
        if (arr[j] - arr[i]) <= K: 
            cnt = max(cnt, j - i + 1)
        else: 
            break

print(max(cnt, 1))  
