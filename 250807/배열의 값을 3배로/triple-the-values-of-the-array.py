a = []
l = []

for i in range(3):
    l = list(map(int, input().split()))
    a.append(l)
for i in range(3):
    for j in range(3):
        print(a[i][j]*3,end=' ')
    print()
