n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def sol(a,b):
    s = 0
    for i in range(a-1, b):
        s+=arr[i]
    return s

for i in queries:
    print(sol(i[0], i[1]))

