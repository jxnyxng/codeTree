word = input()
ee_cnt = 0
eb_cnt = 0

for i in range(1, len(word)):
    if word[i-1]=='e' and word[i]=='e':
        ee_cnt += 1
    elif word[i-1]=='e' and word[i]=='b':
        eb_cnt += 1

print(ee_cnt, eb_cnt)
