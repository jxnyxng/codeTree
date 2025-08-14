M, D = map(int, input().split())

def check_M(M):
    if M<=12:
        return True
    else:
        return False

def check_D(M, D):
    sd = 1
    ed =31
    if M<=7 and M%2==0:
        ed=30
    elif M>7 and M%2!=0:
        ed=30
        
    if M==2:
        ed=28
    
    if D<=ed:
        return True

if check_M(M):
    if check_D(M,D):
        print('Yes')
    else:
        print('No')
else:
    print('No')

