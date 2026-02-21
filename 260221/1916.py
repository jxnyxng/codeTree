# 백준 1916번

# 그래프에 시작 노드마다((도착, 가중치)) 저장
import heapq
MAX = float('inf')

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(node):
    d_table = [MAX] * (N + 1)
    d_table[node] = 0
    pq = []
    heapq.heappush(pq, (0, node))
    
    while pq:
        nowd, now = heapq.heappop(pq)
        
        if nowd > d_table[now]:
            continue
        
        for next_node, we in graph[now]:
            new_dist = nowd + we
            if new_dist < d_table[next_node]:
                d_table[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return d_table

st, ed = map(int, input().split())                            
ans = dijkstra(st)
print(ans[ed])                            
        
        
