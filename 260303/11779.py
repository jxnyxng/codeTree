# 백준 11779번
import heapq

n = int(input())
m = int(input())
road = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    road[a].append((b, c))

A, B = map(int, input().split())    

def dijkstra(st):
    d_table = [float('inf')] * (n+1)
    parent = [0] * (n+1)
    d_table[st] = 0

    pq = []
    heapq.heappush(pq, (0, st))
    
    while pq:
        now_dist, now_node = heapq.heappop(pq)
        
        if now_dist > d_table[now_node]:
            continue
        
        for next_node, w  in road[now_node]:
            new_dist = now_dist + w

            if d_table[next_node] > new_dist:
                d_table[next_node] = new_dist
                parent[next_node] = now_node
                heapq.heappush(pq, (new_dist, next_node))

    return d_table, parent

ans_d, ans_p = dijkstra(A)

path = []
curr = B
while curr != 0:
    path.append(curr)
    curr = ans_p[curr]

path.reverse()
print(ans_d[B])
print(len(path))
print(*path)