dirs = input()
 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_n = 3
x,y = 0,0

for i in dirs:
    now_dir = i
    if i=='L':
        dir_n = (dir_n + 3) % 4
    elif i=='R':
        dir_n = (dir_n + 1) % 4
    else:
        x = x + dx[dir_n]
        y = y + dy[dir_n]

print(x, y) 

