n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# 최대번호까지만 생성
arr = [''] * 10005

for i in range(n):
    arr[x[i]] = c[i]

ans=0

for i in range(0, 10000-k+1):
    keep=0
    for j in range(i, i+k+1):
        if arr[j]=='G':
            keep+=1
        elif arr[j]=='H':
            keep+=2
    ans = max(ans, keep)

print(ans)

