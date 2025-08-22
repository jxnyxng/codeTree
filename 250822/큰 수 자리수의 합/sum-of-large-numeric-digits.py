a, b, c = map(int, input().split())

num = a*b*c

def sol(num):
    if num==0:
        return num
    
    return sol(num//10) + num%10

print(sol(num))
