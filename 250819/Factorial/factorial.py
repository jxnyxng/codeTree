N = int(input())

def sol(n):
    if n==1:
        return 1
    else:
        return sol(n-1) * n
    
print(sol(N))