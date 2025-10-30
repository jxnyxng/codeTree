n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

set_a = set()

for i in range(n):
    command = commands[i]
    nx = x[i]
 
    if command == 'find': 
        if nx in set_a:
            print('true')
        else:
            print('false')
    elif command == 'remove': 
        set_a.remove(nx)
    else:
        set_a.add(nx)
