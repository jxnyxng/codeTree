n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans=0
for i in range(n-k+1):
    keep=sum(arr[i:i+k])
    ans = max(ans, keep)

print(ans)

