n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# 조건 체크 함수
def check(g, h):
    return (g!=0 and h!=0 and g==h) or (g==0 and h!=0) or (g!=0 and h==0)
# gh 저장, 최대 좌푯값 저장
max_idx = 0
arr = ['.'] * 200
for i in range(n):
    arr[pos[i]] = alpha[i]
    max_idx =max(max_idx, pos[i])

ans = 0
# 주어진 조건에 맞는 틀 길이 모두 찾기 -> 틀 길이 최댓값만 저장
# 탐색 시작 지점
for i in range(max_idx+1):
    # 틀 길이 : 탐색 종료 지점 
    for j in range(i, max_idx+1):
        g_cnt = 0
        h_cnt = 0
        for k in range(i, j+1):
            # 조건 체크
            if 'G' == arr[k]:
                g_cnt+=1
            elif 'H' == arr[k]:
                h_cnt+=1
        if check(g_cnt, h_cnt) and arr[i]!='.' and arr[j]!='.':
            # - > 거리는 끝인덱스 - 시작인덱스
            ans = max(ans, j-i)
# for i in arr:
#     print(i, end=' ')

print(ans)
        




