n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
# 가로줄
for i in range(n):
    current_length = 1
    max_length = 1
    
    for j in range(1, n):
        if grid[i][j] == grid[i][j-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
            
    max_length = max(max_length, current_length)
    
    if max_length >= m:
        ans += 1

# 세로줄
for j in range(n):
    current_length = 1
    max_length = 1
    
    for i in range(1, n):
        if grid[i][j] == grid[i-1][j]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
            
    max_length = max(max_length, current_length)
    
    if max_length >= m:
        ans += 1

print(ans)