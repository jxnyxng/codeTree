# 백준 13023

n, m = map(int , input().split())
visited = [False] * n
adjacent = [[] for _ in range(n)]

is_found = False

for _ in range(m):
    a,b = map(int, input().split())

    adjacent[a].append(b)
    adjacent[b].append(a)

def dfs(start , depth):
    global is_found
    visited[start]=True
    
    if depth==5:
        is_found = True
        return
    
    for i in adjacent[start]:
        if visited[i] == False:
            dfs(i , depth+1)

    visited[start]=False

for i in range(n):
    dfs(i ,1)
    if is_found:
        break

print(1 if is_found else 0)