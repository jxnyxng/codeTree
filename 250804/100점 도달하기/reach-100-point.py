N = int(input())
num = N
for i in range(101-N):
    grade=''
    if num>=90:
        grade='A'
    elif num>=80:
        grade='B'
    elif num>=70:
        grade='C'
    elif num>=60:
        grade='D'
    else:
        grade='F'
    num+=1
    print(grade, end=' ')
