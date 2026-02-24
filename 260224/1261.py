# 백준 1261번

# 상하좌우의 노드를 연결한 그래프 만들기
# 다익스트라 돌려서 n,m 위치에 최소비용 저장
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range((N*M)+1)]
wall = []

for _ in range(M):
    line = list(map(int, input()))
    wall.append(line)

cnt = 1
for a in range(M):
    for b in range(N):
        graph[cnt] = []
        if a > 0:  # 상
            graph[cnt].append((cnt-N, wall[a-1][b]))
        if a < M-1:  # 하
            graph[cnt].append((cnt+N, wall[a+1][b]))
        if b > 0:  # 좌
            graph[cnt].append((cnt-1, wall[a][b-1]))
        if b < N-1:  # 우
            graph[cnt].append((cnt+1, wall[a][b+1]))
        cnt += 1

def dijkstra(st):
    d_table = [float('inf')] * (N*M+1)
    d_table[st] = 0
    pq = []
    heapq.heappush(pq, (0, st))
    while pq:
        curr_cost, curr_node = heapq.heappop(pq)

        if curr_cost > d_table[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_cost = curr_cost + weight
            if new_cost < d_table[neighbor]:
                d_table[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return d_table

ans = dijkstra(1)
print(ans[N*M])