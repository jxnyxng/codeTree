word = input()

f = word[0]
s = word[1]

for w in word:
    if w == s:
        print(f, end='')
    else:
        print(w, end='')