N = int(input())
seat = list(input())

# 탐색중 0을 만나면 1 넣기 -> 두번
# 가장 가까운 거리가 최대

# 가장 가까운 거리를 구하는 함수 
def checking(arr):
    left = -1
    min_dist = float('inf')

    for i in range(N):
        if arr[i] == '1':
            if left != -1:
                min_dist = min(min_dist, i - left)
            left = i
    
    return min_dist

ans = 0

# 첫 번째 사람
for i in range(N):
    if seat[i] == '1':
        continue
    
    # 두 번째 사람
    for j in range(i + 1, N):
        if seat[j] == '1':
            continue
        
        nseat = seat.copy()
        nseat[i] = '1'
        nseat[j] = '1'
        
        ans = max(ans, checking(nseat))

print(ans)