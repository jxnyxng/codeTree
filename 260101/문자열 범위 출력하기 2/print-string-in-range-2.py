word = input()
n = int(input())
if len(word)<n:
    n = len(word)
for i in range(n):
    print(word[-1-i], end='')
