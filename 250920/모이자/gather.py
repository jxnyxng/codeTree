n = int(input())
A = list(map(int, input().split()))

#  1 2 3 4 5 6 ...
#  각 집 간 거리가 작은 경우
ans = float('inf')
for i in range(n):
    cnt = 0
    for j in range(n): 
        cnt += (A[j]*(abs(j-i)))
    ans = min(ans, cnt)

print(ans)
