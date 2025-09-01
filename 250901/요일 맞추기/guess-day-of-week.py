m1, d1, m2, d2 = map(int, input().split())
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Mo1=0
Mo2=0

for i in range(1, m1):
    Mo1 += day[i]

for i in range(1, m2):
    Mo2 += day[i]


gap1 = Mo1 + d1
gap2 = Mo2 + d2
    
gap = gap2 - gap1
check = gap%7
if check<0:
    check *= -1
answer = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(answer[check])
