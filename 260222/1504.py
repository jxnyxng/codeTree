# 백준 1504번

# 다익스트라 문제,
# 특정 최단 경로의 길이를 출력하는데, 특정 정점 두개를 지난 경우에만 최단 경로로 인정

# 두가지 경우가 존재
# 1번 정점 - u - v - N
# 1 - v - u - N
# 둘 중에서 최단 경로를 저장하고 없으면 -1 출력
import heapq
MAX = float('inf')

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))
    

def dijkstra(st):
    d_table = [MAX] * (N + 1)
    d_table[st] = 0
    pq = []
    # 거리, 시작노드 저장
    heapq.heappush(pq, (0, st))
    
    while pq:
        now_dist, now_node = heapq.heappop(pq)
        
        if now_dist > d_table[now_node]:
            continue
            
        for next_node, weight in graph[now_node]:
            new_dist = now_dist + weight
            if new_dist < d_table[next_node]:
                d_table[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return d_table

u, v = map(int, input().split())

first_node_start_table = dijkstra(1)
u_node_start_table = dijkstra(u)
v_node_start_table = dijkstra(v)

candidate1 = first_node_start_table[u] + u_node_start_table[v] + v_node_start_table[N]
candidate2 = first_node_start_table[v] + v_node_start_table[u] + u_node_start_table[N]
ans = min(candidate1, candidate2)

print(-1 if ans==MAX else ans)
