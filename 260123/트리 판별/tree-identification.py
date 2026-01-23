# 사이클, 끊긴 부분 체크

# dfs 이후 visited = False 있으면 끊긴거
# 부모 노드가 같은데 연결되면 사이클

n = int(input())
checking = []
bbs = []
aas = set()
tree = [[] for _ in range(10_002)]
ans = 1
for _ in range(n-1):
    a, b = map(int, input().split())
    bbs.append(b)
    aas.add(a)

    if not (b in checking):
        checking.append(b)
    else:
        print(0)
        exit()
    
    tree[a].append(b)

root = -1

for a in aas:
    if not (a in bbs):
        root = a
        break

visited = [False] * (10_002)

def dfs(now, parent):
    for next in tree[now]:
        if next == parent:
            ans = 0
            return 
        else:
            if not visited[next]:
                visited[next] = True
                dfs(next, now)

dfs(root, -1)

for i in tree[root]:
    if not visited[i]:
        ans = 0
        break

print(ans)



