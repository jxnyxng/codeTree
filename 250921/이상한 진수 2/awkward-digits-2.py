a = list(input())

# 바꾼 숫자의 최댓값을 구하려면 0을 1로 만들어야함
# 좌측 1을 바꿔야 유리
# 만약 0이 없으면 최우측 1을 0으로 바꿔야됨

# 좌측부터 탐색해서 0 만나면 1로 교체 후 10진수로 바꾸기
# 0 못 만나면 최우측 1을 0으로 바꾸고 10진수로 출력

for i in range(len(a)):
    if a[i]=='0':
        a[i]='1'
        break

    if i==len(a)-1: #끝날때까지 1발견 못한경우
        a[-1] = 0

# 10진수로 바꾸는 함수
def make_ten(a):
    t=0
    a.reverse()
    for i in range(len(a)):
        if a[i]=='1':
            t+= (2**i)
    
    return t

print(make_ten(a))