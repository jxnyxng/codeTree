n, m = map(int, input().split())

def sol(n, m):
    key = min(n, m)
    big = max(n, m)
    for i in range(key, 0, -1):
        if(big%i==0 and key%i==0):
            return i

print(sol(n,m))
            