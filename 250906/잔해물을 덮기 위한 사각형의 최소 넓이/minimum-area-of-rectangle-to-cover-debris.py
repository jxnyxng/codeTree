x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# 2005 * 2005
# 첫째 직사각형 잘린 부분의 좌하단 우상단 좌표 구하고 넓이 구하기

arr = [[0] * 2005 for _ in range(2005)]
offset = 1002

for j in range(x1[0]+offset, x2[0]+offset):
    for k in range(y1[0]+offset, y2[0]+offset):
        arr[k][j] = 1

for j in range(x1[1]+offset, x2[1]+offset):
    for k in range(y1[1]+offset, y2[1]+offset):
        arr[k][j] = 2

s_i, s_j, b_i, b_j = 2006, 2006, -1, -1

gone = True

for i in range(2005):
    for j in range(2005):
        if arr[i][j]==1:
            gone = False
            s_i = min(s_i, i)
            s_j = min(s_j, j)
            b_i = max(b_i, i)
            b_j = max(b_j, j)

ans = (b_i-s_i+1) * (b_j-s_j+1)
if gone:
    print(0)
else:
    print(ans)

