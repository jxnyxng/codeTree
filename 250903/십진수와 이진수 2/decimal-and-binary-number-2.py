N = list(input())

def bin_to_dec(num):
    s=0 
    num = num[::-1]
    for i in range(len(num)):
        if num[i]=='1':
            s+=2**i 
    return s


def dec_to_bin(num):
    arr = []
    while num!=0:
        arr.append(num%2)
        num//=2
    return arr[::-1]

for i in dec_to_bin(bin_to_dec(N)*17):
    print(i,end='')

        