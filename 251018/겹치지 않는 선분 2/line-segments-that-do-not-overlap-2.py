n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# 선분 두개 비교
# 비교 선분이 앞에서 출발하면 앞에서 끝나야됨
#       뒤에서 출발하면 뒤에서 끝나야됨
# 두 선분이 겹치는지 체크
def checking(l1, l2):
    ori_x = l1[0]
    ori_x2 = l1[1]
    other_x = l2[0]
    other_x2 = l2[1]
 
    # 안겹침  
    if (ori_x < other_x and ori_x2 < other_x2) or (ori_x > other_x and ori_x2 > other_x2):
        return True
    # 겹침
    else:
        return False

ans=0
for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        # 선택한 두 선분을 비교하여 겹치면 f 안겹치면 t 받아오기
        if checking(lines[i], lines[j]):
            cnt+=1
        else:
            break
    if cnt == n-1:
        ans+=1

print(ans)
