a,b,c = map(int, input().split())

if a>b>c or c>b>a:
    print(b)
elif c>a>b or b>a>c:
    print(a)
else:
    print(c)