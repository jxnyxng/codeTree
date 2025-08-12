a, o, c = input().split()
a = int(a)
c = int(c)

def sol(a, o ,c):
    if o=='+':
        return a+c
    elif o=='-':
        return a-c
    elif o=='/':
        return a//c
    elif o=='*':
        return a*c
    else:
        return 'False'

t = sol(a,o,c)

if t=='False':
    print(t)
else:
    print(f'{a} {o} {c} = {t}')