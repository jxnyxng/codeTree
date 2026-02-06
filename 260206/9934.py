# 백준 9934번
k = int(input())
nums = list(map(int, input().split()))

ans = [[] for _ in range(k)]
def sol(level, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    ans[level].append(nums[mid])
    sol(level + 1, start, mid - 1)
    sol(level + 1, mid + 1, end)

sol(0, 0, len(nums) - 1)

for i in range(k):
    print(*ans[i])
