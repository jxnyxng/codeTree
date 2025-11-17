n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# 주어진 위치, 방향에서 바람 시작
# 한칸씩 밀린 결과와 위 아래 행을 비교하여
# 동일한 열에 같은 숫자가 있으면 반대방향으로 파동이 전파된다.

# 두개의 배열을 받아서 같은 열에 같은 숫자가 있는지 확인하는 함수
def is_same(arr1, arr2):
    for i in range(m):
        if arr1[i]==arr2[i]:
            return True 
    return False

# 왼쪽에서 쉬프트하는 함수 : 왼 -> 오
def shift_to_R(i, command):
    global a
    temp=a[i][m-1]
    for j in range(m-1, 0, -1):
        a[i][j] = a[i][j-1]
    a[i][0] = temp

    # 위에 거
    if command!='d' and i!=0 and is_same(a[i], a[i-1]):
        shift_to_L(i-1, 'u')

    # 아래 거
    if command!='u' and i!=n-1 and is_same(a[i], a[i+1]):
        shift_to_L(i+1, 'd')
    
# 오른쪽에서 쉬프트하는 함수 : 오 -> 왼
def shift_to_L(i, command):
    global a
    temp=a[i][0]
    for j in range(m-1):
        a[i][j] = a[i][j+1]
    a[i][m-1] = temp

    if command!='d' and i!=0 and is_same(a[i], a[i-1]):
        shift_to_R(i-1, 'u')

    if command!='u' and i!=n-1 and is_same(a[i], a[i+1]):
        shift_to_R(i+1, 'd')
    


# 위로 진행 중이면 u 아래로 진행중이면 d 처음이면 o
# 메인
for r, d in winds:
    if d == 'L':
        shift_to_R(r-1, 'o')
    else:
        shift_to_L(r-1, 'o')

for row in a:
    print(*row)
