n, m = map(int, input().split())
A = list(map(int, input().split()))

s=0

def sol(m):
    global s
    s += A[m-1]

    if m!=1:
        if m%2==0:
            m//=2
        else:
            m-=1
        sol(m) 

sol(m)

print(s)

