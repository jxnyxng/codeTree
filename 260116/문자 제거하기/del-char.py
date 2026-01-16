word = input()
q = []

for w in word:
    q.append(w)

while len(q)>1:
    idx = int(input())

    if idx >= len(q): idx = -1 

    q.pop(idx)
    print(''.join(q))


