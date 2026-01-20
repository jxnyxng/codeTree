L = input()

for i in range(len(L)+1):
    print(L)
    L = L[-1] + L[:-1]
