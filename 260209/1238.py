# 백준 1238번
# 다익스트라
# 간선 뒤집은 그래프 활용해서 도착지로 오는 모든 노드의 최단경로를 구하고
# 원래 간선 정보로 도착지에서 출발해 각 노드에 도달하는 최단경로를 구한뒤 
# 각 경로를 더해주고 최댓값 출력
import heapq
MAX = float('inf')

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
candidates = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))

def dijkstra(tst, now_graph):
    d_table = [MAX] * (N + 1)
    d_table[tst] = 0
    pq = []
    heapq.heappush(pq, (0, tst))

    while pq:
        d, now = heapq.heappop(pq)

        if d > d_table[now]:
            continue
            
        for next_node, weight in now_graph[now]:
            new_dist = d + weight
            if new_dist < d_table[next_node]:
                d_table[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return d_table

# 도착점으로 오는 다익스트라
start_end_dist = dijkstra(X, reverse_graph)
# 도착점에서 출발하는 다익스트라
end_start_dist = dijkstra(X, graph)
# print(start_end_dist, end_start_dist)
candidates = [start_end_dist[i] + end_start_dist[i] for i in range(1, N + 1)]
print(max(candidates))