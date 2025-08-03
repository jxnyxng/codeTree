a, b = input().split()
if len(a)>len(b):
    print(a, len(a), sep=' ')
elif len(a)<len(b):
    print(b, len(b), sep=' ')
else:
    print('same')