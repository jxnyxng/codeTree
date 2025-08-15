A = input()

def modify(str_):
    str_ = str_[::-1]
    return str_

if A == modify(A):
    print('Yes')
else:
    print('No')
