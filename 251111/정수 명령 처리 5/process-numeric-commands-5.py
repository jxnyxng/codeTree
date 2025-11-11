N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

l = []
for i in range(N):
    nc = command[i]
    nn = num[i]
    
    if nc == "push_back":
        l.append(nn)
    elif nc == "get":
        print(l[nn-1])
    elif nc =="size":
        print(len(l))
    elif nc == "pop_back":
        l.pop(-1)

