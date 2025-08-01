n = int(input())
a = (n%3==0 and n%2!=0) or (n%2==0 and n%5==0)
if a==True:
    print("true")
else:
    print("false")