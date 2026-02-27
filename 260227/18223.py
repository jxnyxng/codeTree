# 백준 18223

# 건우를 데리고 마산에 가는 최단거리와
# 버리고 가는 최단 거리를 비교
# 버리고 가는 최단 거리 < 건우 데리고 가는 최단거리 이면
# GOOD BYE 
# 아니면 SAVE HIM 출력

import heapq

V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(st):
    d_table = [float('inf')] * (V+1)
    d_table[st] = 0
    pq = []
    heapq.heappush(pq, (0, st))
    
    while pq:
        sum_dist, curr_node = heapq.heappop(pq)
        
        if sum_dist > d_table[curr_node]:
            continue
        
        for next_node, weight in graph[curr_node]:
            new_dist = sum_dist + weight
            if d_table[next_node] > new_dist:
                d_table[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return d_table

# 경로1 : 1 -> P -> N
# 경로2 : 1 -> N
start_to = dijkstra(1)
him_to = dijkstra(P)
start_him_end_cost = start_to[P] + him_to[V]
start_end_cost = start_to[V]
print("SAVE HIM" if start_end_cost >= start_him_end_cost else "GOOD BYE")
