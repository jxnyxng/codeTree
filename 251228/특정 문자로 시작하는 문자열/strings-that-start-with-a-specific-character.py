n = int(input())
l = []

for i in range(n):
    l.append(input())

word = input()

cnt = 0
total_length = 0

for w in l:
    if w[0]==word:
        cnt+=1
        total_length+=len(w)

print(cnt, f"{float(total_length/cnt):.2f}")