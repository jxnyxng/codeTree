n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    temp = arr[i]
    if temp%2==0:
        arr[i]//=2

for i in arr:
    print(i, end=' ')

