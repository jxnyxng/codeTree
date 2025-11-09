n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    m = i
    for j in range(i+1, n):
        if arr[j] < arr[m]:
            m = j
    tmp = arr[i]
    arr[i] = arr[m]
    arr[m] = tmp

print(*arr)
        
