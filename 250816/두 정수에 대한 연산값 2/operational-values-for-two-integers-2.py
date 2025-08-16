a, b = map(int, input().split())

def sol(a, b):
    if a<b:
        return print(a+10, b*2)
    else:
        return print(a*2, b+10)

sol(a, b)