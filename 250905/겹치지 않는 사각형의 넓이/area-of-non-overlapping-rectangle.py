x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

arr =[[0] * 2005 for _ in range(2005)]

for i in range(3):
    for j in range(x1[i], x2[i]):
        for k in range(y1[i], y2[i]):
            if i==2:
                arr[j+1001][k+1001]=0
            else:
                arr[j+1001][k+1001]=1
ans=0
for i in arr:
    for j in i:
        if j==1:
            ans+=1

print(ans)
