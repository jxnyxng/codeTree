word = input()
f = input()

for i in range(len(word)-len(f)):
    candidate = ''
    for j in range(i, i+len(f)):
        candidate += word[j]

    if candidate == f:
        print(i)
        exit()

print(-1)