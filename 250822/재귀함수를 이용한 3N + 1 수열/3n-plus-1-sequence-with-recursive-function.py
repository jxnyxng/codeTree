n = int(input())

def sol(num):
    if num==1:
        return 0
    elif num%2==0:
        return sol(num//2) + 1
    else:
        return sol((num*3) + 1) + 1

print(sol(n))