n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 딕셔너리로 개수 카운트하고
# 밸류 키값 크기 기준으로 정렬 후 출력

d1 = dict()
for i in arr:
    d1[i] = d1.get(i, 0) + 1

# 우선순위 밸류->키 정렬
sorted_list = sorted(d1.items(), key=lambda item : (-item[1], -item[0]))

# 정렬된 키값 중 k개만 출력 
for i in range(k):
    print(sorted_list[i][0], end=' ')
