# 백준 5972번
# 1 -> N 으로 가는 최소비용 구하기
import heapq
MAX = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

    
def dijkstra(st):
    d_table = [MAX] * (N+1)
    d_table[st] = 0
    pq = []
    heapq.heappush(pq, (0, st))
    
    while pq:
        now_cost, now_node = heapq.heappop(pq)

        if now_cost > d_table[now_node]:
            continue
            
        for next_node, cost in graph[now_node]:
            new_cost = now_cost + cost
            if new_cost < d_table[next_node]:
                d_table[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    return d_table

ans_table = dijkstra(1)
print(ans_table[N])
