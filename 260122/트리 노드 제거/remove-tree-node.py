n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

# 0 based
# tree 만들고
# 끊을 노드의 visited를 미리 방문처리
# 루트노드에서 시작해서 노드 개수 구하기

tree = [[] for _ in range(n)]
stnode = 0
for idx in range(n):
    pnode, cnode = parent[idx], idx
    if pnode == -1: stnode = idx
    tree[pnode].append(cnode)
    

visited = [False] * n
# visited[stnode] = True
visited[remove_node] = True
ans=0

def dfs(now):
    global ans

    if visited[now]: return 

    visited[now] = True
    
    for next_node in tree[now]:
        if not visited[next_node]:
            ans+=1
            visited[next_node] = True
            dfs(next_node)

dfs(stnode)
print(ans)