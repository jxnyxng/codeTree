# 백준 2170
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort()

start = arr[0][0]
end = arr[0][1]
ans = 0

for i in range(1, n):
    cur_s, cur_e = arr[i]
    
    if cur_s <= end:
        end = max(end, cur_e)
    else:
        ans += end - start
        start = cur_s
        end = cur_e

ans += end - start
print(ans)