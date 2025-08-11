n = int(input())
t = (n//10) + (n%10)

if n%2==0 and t%5==0:
    print('Yes')
else:
    print('No')