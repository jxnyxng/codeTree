n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)
st = 1
visited[st] = True

for _ in range(n-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


def dfs(now):
    for next_node in tree[now]:
        if not visited[next_node]:
            visited[next_node] = True
            parent[next_node] = now
            dfs(next_node)

dfs(st)

for idx in range(2, n+1):
    print(parent[idx])
