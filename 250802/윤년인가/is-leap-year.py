year = int(input())
a=''
if year%4 == 0:
    a='true'
else:
    a='false'

if year%100==0 and year%400!=0:
    a='false'


print(a)

