n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# 점 하나씩 빼서 넓이 구하고 최솟값 출력
ans=[]

# 사각형 만들고 넓이 반환하는 함수
def make(arr):
    min_x, min_y, max_x, max_y = 50000, 50000, -1, -1
    for i in arr:
        min_x=min(min_x, i[0])
        min_y=min(min_y, i[1])
        max_x=max(max_x, i[0])
        max_y=max(max_y, i[1])
    
    return (max_x-min_x) * (max_y-min_y)

# 점 선택
for i in range(n):
    keep=[]
    for j in range(n):
        if j==i:
            continue
        else:
            keep.append(points[j])
    ans.append(make(keep))

ans.sort()
print(ans[0])