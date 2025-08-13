n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def sol(a, b):
    for i in range(0, n1):
        if a[i]==b[0]:
            if checking(i):
                return 'Yes'
    return 'No'


def checking(idx):
    for i in range(n2):
        if a[idx+i] != b[i]:
            return False
    
    return True

print(sol(a,b))