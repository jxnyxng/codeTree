# 백준 18352번
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

queue = deque([X])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

found = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        found = True

if not found: print(-1)