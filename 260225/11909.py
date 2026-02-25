# 백준 11909번
# DP 풀이
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            continue
        
        from_top = float('inf')
        from_left = float('inf')
        
        # 위에서 내려오는 경우
        if i > 0:
            diff = board[i][j] - board[i-1][j]
            cost = diff + 1 if diff >= 0 else 0
            from_top = dp[i-1][j] + cost
            
        # 왼쪽에서 오는 경우
        if j > 0:
            diff = board[i][j] - board[i][j-1]
            cost = diff + 1 if diff >= 0 else 0
            from_left = dp[i][j-1] + cost
            
        dp[i][j] = min(from_top, from_left)

print(dp[N-1][N-1])

# 다익스트라
# 현재 숫자와 이동할 칸의 숫자를 비교 후
# 현재 숫자가 더 크면 코스트는 0
# 현재 숫자가 더 작으면 (이동할 칸의 숫자+1 - 현재 숫자)가 코스트 
# d_table[N*N] 의 코스트와 비교하여 진행 여부 결정
# import heapq

# N = int(input())
# graph = [[] for _ in range((N*N)+1)]
# costs = []

# for i in range(N):
#     costs.append(list(map(int, input().split())))

# # print(costs)
# cnt = 1
# for a in range(N):
#     for b in range(N):
#         if a > 0:  # 상
#             graph[cnt].append((cnt-N, costs[a-1][b]))
#         if a < N-1:  # 하
#             graph[cnt].append((cnt+N, costs[a+1][b]))
#         if b > 0:  # 좌
#             graph[cnt].append((cnt-1, costs[a][b-1]))
#         if b < N-1:  # 우
#             graph[cnt].append((cnt+1, costs[a][b+1]))
#         cnt += 1

# def dijkstra(st):
#     d_table = [float('inf')] * ((N * N) + 1)
#     d_table[st] = 0
#     pq = []
#     heapq.heappush(pq, (costs[0][0], 0, st))
    
#     while pq:
#         now_cost, btn_cnt, now_node = heapq.heappop(pq)

#         for next_node, next_cost in graph[now_node]:
#             new_btn_cnt = btn_cnt
#             if next_cost >= now_cost:
#                 new_btn_cnt = btn_cnt + (next_cost - now_cost + 1)

#             if d_table[next_node] > new_btn_cnt:
#                 d_table[next_node] = new_btn_cnt
#                 heapq.heappush(pq, (next_cost, new_btn_cnt, next_node))
#     return d_table                

# ans_table = dijkstra(1)
# print(ans_table[N*N])

# -> 메모리 초과...
