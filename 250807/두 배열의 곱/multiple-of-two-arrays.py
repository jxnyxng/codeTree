array1 = [list(map(int, input().split())) for _ in range(3)]
t = input()
array2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(array1[i][j]*array2[i][j], end=' ')
    print()
