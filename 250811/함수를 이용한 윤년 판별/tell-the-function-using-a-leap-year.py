y = int(input())


def sol(y):
    answer = 'false'
    if y%4==0:
        answer = 'true'
    if y%100==0 and y%400!=0:
        answer = 'false'
    return answer
    

print(sol(y))