n = int(input())
arr = [int(input()) for _ in range(n)]
arr.append(-1)

cnt=0
ans=0
for i in range(0, n):
    cnt+=1
    ans = max(ans,cnt) 
    if arr[i] != arr[i+1]:
        cnt=0


print(ans)