# 백준 1806번

N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))
new_arr = [0] * (len(arr))

for i in range(1, len(arr)):
    new_arr[i] = new_arr[i-1] + arr[i]

ans = float('inf')
left = 0
right = 1

while right < len(new_arr):
    current_sum = new_arr[right] - new_arr[left]
    
    if current_sum >= S:
        ans = min(ans, right - left)
        left += 1
    elif current_sum < S:
        right += 1

print(0 if ans == float('inf') else ans)