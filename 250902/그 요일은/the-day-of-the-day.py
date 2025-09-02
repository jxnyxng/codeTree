m1, d1, m2, d2 = map(int, input().split())
A = input()

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30 ,31 ,30, 31]
date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
start = 0
end = 0
for i in range(m1):
    start+=days[i]
for i in range(m2):
    end+=days[i]

start+=d1
end+=d2

check = (end-start)+1
ans = 0

for i in range(check%7):
    if date[i]==A:
        ans=1
        break
ans += check//7
print(ans)

