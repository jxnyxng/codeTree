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
            first = arr[i]
            second = arr[j]+arr[k]
            third = s-arr[i]-arr[j]-arr[k]

            # print(new_arr)
            if not(first==second or second==third or first==third):
                new_arr = [first, second, third]
                ans = min(ans, (max(new_arr)-min(new_arr)))

if ans==float('inf'):
    print(-1)
else:
    print(ans)
