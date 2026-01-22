n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

tree = [[] for _ in range(n)]
stnode = 0
for idx in range(n):
    pnode, cnode = parent[idx], idx
    if pnode == -1: 
        stnode = idx
    else: 
        if idx == remove_node:
            continue
        tree[pnode].append(cnode)
    
ans=0
def dfs(now):
    global ans

    if not tree[now]:
        ans+=1
        return

    has_child = False
    for next_node in tree[now]:
        if next_node != remove_node:
            has_child = True
            dfs(next_node)
    
    if not has_child:
        ans += 1
if stnode != remove_node:
    dfs(stnode)
print(ans)
