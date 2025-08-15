A = input()

def rev(a):
    rl = list(a)
    rl.reverse()
    r=''
    
    for i in rl:
        r+=i

    return r

if rev(A) == A:
    print('Yes')
else:
    print('No')
