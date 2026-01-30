a, b = map(int, input().split())
c, d = map(int, input().split())
arr = [0] * 105
for i in range(a,b):
    arr[i] = 1
for i in range(c,d):
    arr[i] = 1
cnt=0
for i in range(105):
    if arr[i]==1: cnt+=1

print(cnt)
