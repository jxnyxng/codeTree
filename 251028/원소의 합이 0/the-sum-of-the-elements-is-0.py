n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 0~3행 중 네개의 수를 골라 합이 0이 되는 서로 다른 경우의 수를 출력
# ab에 있는 경우가 가능한지 cd에 있는 값으로 비교 

from collections import Counter
 
list_ab = []
for i in range(n):
    for j in range(n):
        list_ab.append(A[i] + B[j])
 
list_cd = []
for i in range(n): 
    for j in range(n):
        list_cd.append(C[i] + D[j])
 
count_cd = Counter(list_cd)

ans = 0
for num_ab in list_ab:  
    ans += count_cd[-num_ab]

print(ans) 