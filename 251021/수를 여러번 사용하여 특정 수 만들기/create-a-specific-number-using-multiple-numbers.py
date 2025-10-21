A, B, C = map(int, input().split())

# a를 i번 더할때 b를 j번 더하기 반복
# c초과시 중지
ans=0
for i in range(1001):
    for j in range(1001):
        na = i*A
        nb = j*B

        # 범위 내에 있다면 최댓값과 비교
        if na+nb<=C:
            ans = max(ans, na+nb)
        else:
            break
print(ans)



