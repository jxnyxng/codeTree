word = input()
st = []
for i in range(len(word)):
    if i%2==1:
        st.append(word[i])

for _ in range(len(st)):
    print(st.pop(), end='')
    