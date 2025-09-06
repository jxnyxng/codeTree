n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# 전체 배열 205 * 205
# 주어진 사각형 범위 -> 1
# 배열 한칸 넓이 = 1 이니까 1의 개수가 정답

arr= [[0] * 205 for _ in range(205)]
offset = 102

for i in range(n):
    n_x = x[i] + offset
    n_y = y[i] + offset
    for j in range(n_x, n_x+8):
        for k in range(n_y, n_y+8):
            arr[j][k] = 1

ans = 0

for i in arr:
    for j in i:
        if j==1:
            ans+=1
print(ans)