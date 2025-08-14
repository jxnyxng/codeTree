Y, M, D = map(int, input().split())

def yoon(Y):
    if Y%4==0 and Y%100!=0:
        return True
    elif Y%4==0 and Y%100==0 and Y%400==0:
        return True
    else:
        return False

def Max_D(M):
    if M<=7:
        if M%2!=0:
            return 31
        else:
            return 30
    else:
        if M%2!=0:
            return 30
        else:
            return 31

if M==2 and D==29:
    if yoon(Y):
        print('Winter')
    else:
        print(-1)
else:
    md = Max_D(M)
    if md<D:
        print(-1)
    elif M>=3 and M<=5:
        print('Spring')
    elif M>=6 and M<=8:
        print('Summer')
    elif M>=9 and M<=11:
        print('Fall')  
    else:
        print('Winter')  