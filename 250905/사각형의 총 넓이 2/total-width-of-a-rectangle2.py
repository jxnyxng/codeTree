n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

arr = [[0] * 205 for _ in range(205)]

for l in range(n):
    for i in range(x1[l], x2[l]):
        for j in range(y1[l], y2[l]):
            arr[i+100][j+100] += 1
s = 0
for i in arr:
    for j in i:
        if j!=0:
            s+=1

print(s)