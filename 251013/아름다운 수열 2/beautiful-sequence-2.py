N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
ans=0
# 차례대로 M개의 숫자를 선택하여 만든 배열에
# 기존에 주어진 배열의 숫자들이 모두 존재하면 카운트
for i in range(N-M+1): #시작 지점 설정
    cnt=0
    partOfA=[]
    for j in range(i, i+M):
        partOfA.append(A[j])
    partOfA.sort()
    
    for k in range(M):
        if partOfA[k]!=B[k]:
            break
        if k==M-1:
            ans+=1

    
print(ans)
    
