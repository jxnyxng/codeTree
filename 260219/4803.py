# 백준 4803번
index = 1
# 부모 노드를 받아서 방문, 사이클 판별하는 함수
def dfs(now, prev):
    global has_cycle
    visited[now] = True
    
    for next_node in graph[now]:
        if next_node == prev:
            continue
            
        if not visited[next_node]:
            dfs(next_node, now)
        else:
            # 직전 노드가 아닌데 방문한 적이 있다면 사이클
            has_cycle = True    
        
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
        
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    cnt = 0
    
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)        
    
    # 2. 탐색돌려서 방문 체크
        # 부모 노드가 될 수 있는건 1~n 노드 모두
        # 1번 노드부터 부모노드로 시작, (방문 안 한 경우만)
        # 체크하면서 카운트 후 출력

    for now_pnode in range(1, n + 1):
        if not visited[now_pnode]:
            has_cycle = False
            dfs(now_pnode, 0)
            
            if not has_cycle:
                cnt += 1

    if cnt == 0:
        print(f"Case {index}: No trees.")
    elif cnt == 1:
        print(f"Case {index}: There is one tree.")
    else:
        print(f"Case {index}: A forest of {cnt} trees.")  

    index += 1