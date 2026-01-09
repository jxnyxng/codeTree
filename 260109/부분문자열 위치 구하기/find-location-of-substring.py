word = input()
f = input()

for i in range(1, len(word)):
    if word[i-1] + word[i] == f:
        print(i-1)
        exit()

print(-1)