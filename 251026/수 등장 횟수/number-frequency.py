n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

from collections import defaultdict

cnt = defaultdict(lambda : 0) 

for i in arr:
    cnt[i] += 1 
for i in nums:
    print(cnt[i], end=' ')