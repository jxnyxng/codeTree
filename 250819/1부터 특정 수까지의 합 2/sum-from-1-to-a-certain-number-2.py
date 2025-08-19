N = int(input())

def s(n):
    if n==1:
        return 1

    return s(n-1) + n 

print(s(N))
