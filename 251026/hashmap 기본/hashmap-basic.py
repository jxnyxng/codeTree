n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

dict1 = dict()

for i in range(n):
    command = commands[i][0]
    key = commands[i][1] 
    
    if command=='add':
        dict1[key] = commands[i][2]
    elif command=='find':
        if key in dict1:
            print(dict1[key])
        else:
            print('None')
    else:
        del dict1[key]


