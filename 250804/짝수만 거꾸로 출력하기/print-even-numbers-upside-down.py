num = int(input())
L = list(map(int, input().split()))
for i in range(num):
    now=L[len(L)-i-1]
    if now%2==0:
        print(now, end=' ')
