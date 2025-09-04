n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0] * 205

for i in segments:
    for j in range(i[0]+101, i[1]+101):
        arr[j] += 1

ans = 0
for i in arr:
    ans = max(ans, i)
print(ans)
