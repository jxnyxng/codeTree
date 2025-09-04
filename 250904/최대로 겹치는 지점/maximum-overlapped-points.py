n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 정답 배열 크기 105
# 끝점 포함 -> 주어진 구간 양 끝 포함

arr = [0] * 105

for i in segments:
    st = i[0]
    ed = i[1]
    for j in range(st, ed+1):
        arr[j] += 1

ans = 0
for i in arr:
    ans = max(ans, i)

print(ans)