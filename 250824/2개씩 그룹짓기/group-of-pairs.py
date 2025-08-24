n = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 0

for i in range(n):
    ans = max(ans, nums[i]+nums[2*n - i - 1])
    
print(ans)
