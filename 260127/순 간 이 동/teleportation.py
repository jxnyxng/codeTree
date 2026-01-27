A, B, x, y = map(int, input().split())

# x에서 사용하는 경우
# (B - y) + (A - x)
# y에서 사용하는 경우
# (B - x) + (A - y)

# 중에서 최솟값

print(min((abs(B-y)+abs(A-x)), (abs(B-x)+abs(A-y)), abs(A-B)))


