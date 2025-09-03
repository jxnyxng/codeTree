n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0] * (n+1)

for i in commands:
    for j in range(i[0], i[1]+1):
        arr[j] += 1 

ans = 0

for i in arr:
    ans = max(ans, i)

print(ans)