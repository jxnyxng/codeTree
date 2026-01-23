# 사이클, 끊긴 부분 체크

# dfs 이후 visited = False 있으면 끊긴거
# 부모 노드가 같은데 연결되면 사이클

n = int(input())
checking = []
tree = [[] for _ in range(n+1)]
ans = 1
for _ in range(n-1):
    a, b = map(int, input().split())

    if not (b in checking):
        checking.append(b)
    else:
        ans = 0
        break
    
    # tree[a].append(b)

# visited = [False] * (n+1)

# ans = 1
# def dfs(now, parent):
#     for next in tree[now]:
#         if next == parent:
#             ans = 0
#             return 
#         elif not visited[next]:
#             visited[next] = True
#             dfs(next, now)

# dfs(1, -1)

# for i in range(1, n+1):
#     if not visited[i]:
#         ans = 0
#         break

print(ans)

