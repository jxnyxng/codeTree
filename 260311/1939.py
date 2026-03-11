# 백준 1939번

# 출발 노드 -> 도착 노드
# d_table[도착노드] 값이 최대무게
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))    
    graph[b].append((a, c))

st, ed = map(int, input().split())    

def dijkstra(st):
    d_table = [0] * (N+1)
    d_table[st] = float('inf')
    pq = []
    heapq.heappush(pq, (-float('inf'), st))

    while pq:
        weight, now_node = heapq.heappop(pq)
        weight = -weight

        if d_table[now_node] > weight:
            continue

        for next_node, nw in graph[now_node]:
            next_weight = min(weight, nw)
            if d_table[next_node] < next_weight:
                d_table[next_node] = next_weight
                heapq.heappush(pq, (-next_weight, next_node))
    return d_table

ans = dijkstra(st)
print(ans[ed])    