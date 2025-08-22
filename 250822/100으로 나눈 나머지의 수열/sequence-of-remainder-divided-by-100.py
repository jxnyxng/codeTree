N = int(input())

ans = 0

def sol(num):
    if num==1:
        return 2
    elif num==2:
        return 4
    else:
        return (sol(num-1) * sol(num-2)) % 100


print(sol(N))