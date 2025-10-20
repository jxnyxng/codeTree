X, Y = map(int, input().split())

#  두 숫자 사이의 수들을 모두 변수에 담기
# 세트로 담아 중복 제거 후 길이가 2가 아니면 패스

cnt=0
for i in range(X, Y+1):
    nnum = list(str(i))
    if len(set(nnum))!=2:
        continue
    else:
        keep = nnum[0]
        a=0
        b=0
        for k in nnum:
            if keep==k:
                a+=1
            else:
                b+=1
        if a==1 or b==1:
            cnt+=1

print(cnt)

    
    