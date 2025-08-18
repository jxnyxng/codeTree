n = int(input())

def print_star(a):
    global n
    for i in range(n-a+1):
        print('*', end='')

def sol(num):
    if num==0:
        return
    else:
        print_star(num)
        print()
        sol(num-1)
    

sol(n)