A = list(input())
A.append('end')

# 여는괄호 두개되면 멈추고
# 닫는괄호 연속 두개 찾기
# 인덱스는 1씩 증가

ans=0
for i in range(len(A)):
    if A[i]=='(' and A[i+1]=='(':
        for j in range(i+2, len(A)):
            if A[j]==')' and A[j+1]==')':
                ans+=1

print(ans)








