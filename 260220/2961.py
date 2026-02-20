# 백준 2961번
from itertools import combinations

n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

ans = float('inf')
for i in range(1, n+1):
    for a in combinations(arr, i):
        sour = 1
        bitter = 0
        for s, b in a:
            sour *= s
            bitter += b
        ans = min(ans, abs(sour-bitter))
        
print(ans)