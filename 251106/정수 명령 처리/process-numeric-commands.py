N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

stack = []

for i in range(N):
    c = command[i]
    if c == "push":
        stack.append(value[i])
    elif c == "size":
        print(len(stack))
    elif c == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == "top":
        print(stack[-1])
    elif c == "pop":
        print(stack.pop())

