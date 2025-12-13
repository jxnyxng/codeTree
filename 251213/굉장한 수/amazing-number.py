num = int(input())

def checking(num):
    return (num%2==1 and num%3==0) or (num%2==0 and num%5==0)
    
print("true" if checking(num) else "false")