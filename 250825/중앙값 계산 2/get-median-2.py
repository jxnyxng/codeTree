n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n, 2):
    arr2 = []
    for j in range(0, i+1):
        arr2.append(arr[j])
        arr2.sort()
    print(arr2[len(arr2)//2], end=' ')


        

