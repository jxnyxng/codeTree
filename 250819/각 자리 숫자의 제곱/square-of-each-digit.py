N = int(input())

def sol(n):
    if n//10==0:
        return (n%10)**2
    
    return sol(n//10) + (n%10)**2

print(sol(N))