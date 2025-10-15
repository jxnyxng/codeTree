n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# 모든 숫자를 만들어보고 주어진 숫자들로 확인 했을 때 동일한 결과가 나오면 카운트
 
ans=0
# 메인 -> 숫자 만들기
for i in range(1, 10):
    for j in range(1, 10):
        for l in range(1, 10):
            # 서로 다른 숫자인지 확인
            if i==j or j==l or i==l:
                continue

            # 체크 결과 
            result = True
            # 후보 숫자 생성
            can_num = str(i) + str(j) + str(l)
            for check_idx in range(n):
                # 주어진 숫자 차례대로 생성
                check_num = str(a[check_idx])
                # 포인트 체크할 변수
                one = 0
                two = 0

                # 각 자릿수가 정답인지, 있긴 한건지 체크
                for k in range(3):
                    if can_num[k] == check_num[k]:
                        one+=1
                        continue
                    if can_num[k] in check_num:
                        two+=1
                # 체크한 결과의 포인트가 다르면 후보숫자 탈락
                if one != b[check_idx] or two != c[check_idx]:
                    result = False
                    break
            # 체크한 포인트가 모두 동일하면 카운트
            if result:
                ans+=1
    
print(ans)
                




            

