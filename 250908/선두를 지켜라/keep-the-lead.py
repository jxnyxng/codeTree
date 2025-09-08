n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# 시간별 거리 기록하는 배열을 각각 만들고, 시간이 흐름에 따라 거리를 기록
# 기록된 배열을 비교하며 각 시각에사 거리 값이 누가 더 큰지 체크

# 각 거리 배열 -> 인덱스 번호 : 시간
a_time, b_time = [0] * 1000005, [0] * 1000005
start=1

# a의 기록 체크
for i in range(n):
    for j in range(start, start+t[i]):
        a_time[j] = a_time[j-1] + v[i]
    start = start+t[i]

start=1
# b의 기록 체크
for i in range(m):
    for j in range(start, start+t2[i]):
        b_time[j] = b_time[j-1] + v2[i]
    start = start+t2[i]

#초기 선두 지정
head = ''
# 추월 체크
ans = 0
for i in range(1, start+1):
    if a_time[i]<b_time[i]:
        if head=='a':
            # print(i)
            ans+=1
            head='b'
        elif head=='':
            head='b'

    elif a_time[i]>b_time[i]:
        if head=='b':
            # print(i)            
            ans+=1
            head='a'
        elif head=='':
            head='a'

print(ans)

# for i in range(0, 20):
#     print(a_time[i], end=' ')
# print()
# for i in range(0, 20):
#     print(b_time[i], end=' ')
