num = int(input())
matrix = [[0]*num for i in range(num)]

for i in range(num):
    if i%2==0 :
        for j in range(num):
            matrix[j][i] = j+1
    else:
        for j in range(num-1,-1,-1):
            matrix[j][i] = num-j
for i in range(num):
    for j in range(num):
        print(matrix[i][j], end='')
    print()
            
