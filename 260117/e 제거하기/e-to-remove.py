word=input()
run = False

for w in word:
    if run or w!='e': print(w, end='')

    if w == 'e': run = True
        