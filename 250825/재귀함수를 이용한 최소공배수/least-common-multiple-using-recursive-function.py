n = int(input())
arr = list(map(int, input().split()))

answer = arr[0]

def gcd(n, m):
    if n>m:
        temp = n
        n = m
        m = temp

    if n==0:
        return m
    else:
        return gcd(n, m%n)

def sol(n, m):
    return int(n*m/gcd(n,m))

for i in arr:
    answer = sol(i, answer)

print(answer)