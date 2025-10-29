n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = set(arr)
# 완탐 : i j 번째 수들을 골라서 k가 되면 카운트

# k-arr[i]-> 이 값이 딕셔너리에 존재하면 카운트,
# 중복된 수 -> 딕셔너리로 관리 가능
 
d1 = dict()
cnt=0

for num in arr: 
    c = k - num
    if c in d1:
        cnt += d1[c]
     
    d1[num] = d1.get(num, 0) + 1
    


print(cnt)

