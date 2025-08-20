N = int(input())

def sol(n):
    if n%2==0:
        print(s(2))
    else:
        print(s(1))


def s(n):
    if n==N:
        return n
    else:
        return s(n+2) + n

sol(N)