word = list(input())
first = word[0]
second = word[1]

for w in word:
    if w==first:
        print(second, end='')
    elif w==second:
        print(first, end='')
    else:
        print(w, end='')