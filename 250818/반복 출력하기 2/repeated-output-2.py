n = int(input())

def p(n):
    print("HelloWorld")

    if n==1:
        return
    else:
        p(n-1)

p(n)