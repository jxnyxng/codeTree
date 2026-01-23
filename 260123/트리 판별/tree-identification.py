import sys
sys.setrecursionlimit(10**9)
# 사이클, 끊긴 부분 체크

# dfs 이후 visited = False 있으면 끊긴거
# 부모 노드가 같은데 연결되면 사이클

n = int(input())

tree = [[] for _ in range(10001)]
deg = [0] * 10001
used = [False] * 10001
visited = [False] * 10001
ans = 1

# 입력 받기
for _ in range(n):
    try:
        line = sys.stdin.readline()
        if not line: break
        a, b = map(int, line.split())
        
        tree[a].append(b)
        deg[b] += 1
        used[a] = True
        used[b] = True
    except: break

root = 0

for i in range(1, 10001):
    if used[i] and deg[i] == 0:
        if root != 0:
            ans = 0
        root = i

if root == 0:
    ans = 0

for i in range(1, 10001):
    if used[i] and i != root and deg[i] != 1:
        ans = 0

def dfs(now):
    visited[now] = True
    for next_node in tree[now]:
        if not visited[next_node]:
            dfs(next_node)

if ans == 1 and root != 0:
    dfs(root)

for i in range(1, 10001):
    if used[i] and not visited[i]:
        ans = 0

print(ans)