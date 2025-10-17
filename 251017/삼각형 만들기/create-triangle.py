n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

#넓이 드베 반환
def cal(p1, p2, p3):
    # 조건을 만족 x
    # 1. y축이랑 평행한 두 점 없음
    if not(p1[0] == p2[0] or p1[0] == p3[0] or p2[0] == p3[0]):
        return 0

    # 2. x축이랑 평행한 두 점 없음
    if not(p1[1] == p2[1] or p1[1] == p3[1] or p2[1] == p3[1]):
        return 0

    # 넓이 
    a = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
    b = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    return abs(a - b)

answer =0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            answer = max(answer, cal(points[i], points[j], points[k]))

print(answer)