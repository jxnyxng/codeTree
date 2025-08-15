a, b = map(int, input().split())

def sol(a,b):
    if a<b:
        return print(f'{a*2} {b+25}')
    else:
        return print(f'{a+25} {b*2}')

sol(a,b)
