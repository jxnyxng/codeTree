n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, l = map(int, input().split())

    tree[n1].append((n2, l))
    tree[n2].append((n1, l))

# 한 정점에서 제일 멀리있는 정점 찍고
# 그 정점에서 제일 멀리있는 정점이 트리의 지름

visited = [False] * (n+1)
visited[1] = True
farthest_node = 0
max_dist = 0

def dfs(now_node, now_length):
    global farthest_node, max_dist
    
    if now_length > max_dist:
        max_dist = now_length
        farthest_node = now_node

    for next_node, next_length in tree[now_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, now_length + next_length)

visited = [False] * (n+1)
visited[1] = True
dfs(1, 0)

start_node = farthest_node
max_dist = 0
visited = [False] * (n+1)
visited[start_node] = True
dfs(start_node, 0)

print(max_dist)