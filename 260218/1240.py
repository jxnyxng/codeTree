# 백준 1240번

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, d = map(int, input().split())    
    tree[n1].append((n2, d))
    tree[n2].append((n1, d))    
    
q = []
for _ in range(M):
    n1, n2 = map(int, input().split())
    q.append((n1, n2))

def dfs(nown, endn, sumd):
    visited[nown] = True
    for nextn, nowd in tree[nown]:
        if nextn == endn:
            print(sumd+nowd)
            return
        elif not visited[nextn]:
            dfs(nextn, endn, sumd+nowd)
            
for st, ed in q:
    visited = [False] * (N+1)
    dfs(st, ed, 0)