arr = list(map(int, input().split()))
ans=float('inf')
s = sum(arr)
# 1명 고르기
for i in range(5):
# 2명 고르기 
    for j in range(5):
        if i==j:
            continue
        for k in range(j+1, 5): 
            if k==i:
                continue

            # print(new_arr)
            if not(arr[j]+arr[k] == arr[i] and arr[i]==s-arr[i]-arr[j]-arr[k]):
                new_arr = [arr[j]+arr[k], arr[i], s-arr[i]-arr[j]-arr[k]]
                ans = min(ans, (max(new_arr)-min(new_arr)))

if ans==float('inf'):
    print(-1)
else:
    print(ans)
