N = int(input())

def print_num(n):
    if n==0:
        return
    else:
        print(n, end=' ')
        print_num(n-1)
    print(n, end=' ')

print_num(N)