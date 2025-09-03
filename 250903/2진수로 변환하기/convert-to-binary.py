n = int(input())

answer = []
while n>=2:
    answer.append(n%2)
    n //= 2

answer.append(n)

for i in answer[::-1]:
    print(i, end='')