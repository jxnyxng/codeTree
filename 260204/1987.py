# 백준 1987
R, C = map(int, input().split())

arr = [[''] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(R):
    line = input()
    for j in range(C):
        arr[i][j] = line[j]
        
ans = 0

def dfs(x, y, count, v):
    global ans
    ans = max(ans, count)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] not in v:
                v.add(arr[nx][ny])
                dfs(nx, ny, count + 1, v)
                v.remove(arr[nx][ny])

start_set = set([arr[0][0]])
dfs(0, 0, 1, start_set)

print(ans)