word = input()
f = input()
cnt = 0
for i in range(1, len(word)):
    if word[i-1]+word[i] == f:
        cnt+=1

print(cnt)