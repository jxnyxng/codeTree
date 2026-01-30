n = int(input())
arr = [0]*105
for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        arr[j] += 1
        if arr[j] == n:
            print('Yes')
            exit()

print('No')

