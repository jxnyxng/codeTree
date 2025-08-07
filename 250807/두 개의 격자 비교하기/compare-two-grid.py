N, M = map(int, input().split())
arr = []
arr2 = []

for i in range(N):
    arr.append(list(map(int, input().split())))


for i in range(N):
    arr2.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(M):
        if arr[i][j] == arr2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()

    
