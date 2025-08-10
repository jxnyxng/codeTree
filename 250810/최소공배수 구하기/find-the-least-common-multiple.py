n, m = map(int, input().split())
small = min(n,m)
big = max(n,m)

for i in range(1, big+1):
    temp = small*i
    if temp%big==0:
        print(temp)
        break
