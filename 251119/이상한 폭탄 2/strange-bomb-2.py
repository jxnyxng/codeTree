N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# 숫자 하나씩 잡기 -> N
# 거리 내의 동일 원소 체크 -> N
# 처음에서 시작해 뒤로 찾으면, 이전 거 안 봐도 됨
def in_range(idx):
    return 0<=idx<N
# 거리 안에 동일 숫자가 있는지 확인하는 함수
def checking(idx, now_num):

    for i in range(idx+1, idx+K+1):

        if not in_range(i):
            return -1

        if num[i]==now_num:
            return now_num
    
    return -1
ans = -1

for idx in range(N):
    start_num = num[idx]
    ans = max(ans, checking(idx, start_num))

print(ans)