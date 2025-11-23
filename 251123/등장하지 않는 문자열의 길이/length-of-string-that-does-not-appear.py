N = int(input())
str = input()

# 등장할 수 있는 문자열의 모든 경우를 세트에 저장, 세트에 있으면 카운트

length=0
check = set() 
# 문자열 시작 부분
for i in range(N):
    start_idx = i
    # 문자열 끝 부분
    for j in range(N):
        # 문자 만들기
        word = ''
        for k in range(i, j+1):
            word += str[k]
        if word in check:
            length = max(length, len(word))
        else:
            check.add(word)

print(length+1)
