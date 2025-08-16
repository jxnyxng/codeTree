A = input()

def sol(a):
    c = a[0]
    for i in a:
        if i!=c:
            return True
    
    return False

if sol(A):
    print('Yes')
else:
    print('No')
