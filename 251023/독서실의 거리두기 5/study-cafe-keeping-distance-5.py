n = int(input())
arr = list(map(int, input().split()))

# 배열의 하나의 숫자를 두배, 하나는 제거한뒤 인접한 차이 반환하는 함수
def sol(ori_arr, i, j):
    a = ori_arr.copy() 
    a[i] = a[i] * 2 
    a.pop(j)

    re = 0
    for c in range(len(a) - 1):
        re += abs(a[c] - a[c+1])
    return re


# 메인
ans = float('inf')
for i in range(n): #두배할거
    for j in range(n): #제거할거 
        if i == j:
            continue 
        ans = min(ans, sol(arr, i, j))

print(ans)