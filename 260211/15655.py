# 백준 15655번
n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
ans = []
def sol(start, path):
    
    if len(path) == m:
        ans.append(path)
        return
    
    for i in range(start, n):
        sol(i+1, path + [nums[i]])

sol(0, [])

for p in ans:
    print(*p)