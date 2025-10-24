n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
# 최대 a값 이하의 돌들만 밟아서 1~N 도달 가능한지
def check(A):
    if arr[0] > A:
        return False
    last_idx = 0
    for i in range(1,n):
        if arr[i] > A:
            continue
        # 숫자상 밟을 수 있으면 점프력이 되는지 확인 
        if i - last_idx <= k:
            last_idx=i
        else:
            return False
    # 최종적으로 N번째 돌에 도착했는지 반환
    return last_idx == n-1
   
for a in range(1, 101):
    if check(a):
        print(a)
        break


