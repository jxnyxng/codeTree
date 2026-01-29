x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

arr = [[0] * 105 for _ in range(105)]

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        arr[i][j] = 1

for i in range(a1, a2+1):
    for j in range(b1, b2+1):
        if arr[i][j] == 1:
            print("overlapping")
            exit()

print("nonoverlapping")
