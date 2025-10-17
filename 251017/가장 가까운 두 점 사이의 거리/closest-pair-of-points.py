n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# 거리 계산하는 함수
def cal(x1, y1, x2, y2):
    return ((x1-x2)**2) + ((y1-y2)**2)
 
arr = []
# 메인
for i in range(n):
    for j in range(i+1, n):
        arr.append(cal(x[i], y[i], x[j], y[j]))


print(min(arr[:]))

