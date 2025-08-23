N = int(input())

def sol(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return sol(num//3) + sol(num-1)

print(sol(N))