n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
arr1 = set(arr1)

for i in arr2:
    if i in arr1:
        print(1, end=' ')
    else:
        print(0, end=' ')