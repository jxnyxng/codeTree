n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

parent = [0] * (n+1)
for n1, n2 in edges:
    parent[n2] = n1

for p in range(2, n+1):
    print(parent[p])