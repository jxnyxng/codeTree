# 백준 1967 
# 트리의 지름
# 트리 dfs 돌리기 -> 자식 노드로 내려가면서 길이를 측정
# 두번 돌리는데,
# 아무 노드 잡고 말단 노드 찾고
# 말단 노드에서 시작해서 가장 멀리 떨어진 노드를 찾기
# 두번째의 길이가 트리의 지름

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def dfs(start):
    visited = [False] * (n + 1)
    stack = [(start, 0)]
    visited[start] = True
    
    farthest_node = start
    max_length = 0
    
    while stack:
        node, length = stack.pop()
        
        if length > max_length:
            max_length = length
            farthest_node = node
        
        for neighbor, weight in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append((neighbor, length + weight))
    
    return farthest_node, max_length

farthest_node, _ = dfs(1)
_, diameter = dfs(farthest_node)

print(diameter)