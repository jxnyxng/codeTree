matrix = []
sum=0

for _ in range(4):
    matrix.append(list(map(int, input().split())))

for i in range(4):
    for j in range(0,i+1):
        sum += matrix[i][j]

print(sum)