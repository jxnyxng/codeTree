commands = input()

# 0,0 에서 북쪽 보고 시작
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]
# dr = {'L':0, 'R':1, 'F':2, 'W':3}

x,y = 0,0
nidx = 0
# 회전에는 1초 걸린다 -> 회전만 하고 초 증가시키면 됨
for i in range(len(commands)):
    nin = commands[i]

    if nin=='F':
        x += dxs[nidx]
        y += dys[nidx]
    elif nin=='L':
        nidx = (nidx+1)%4
    else:
        nidx = (nidx+3)%4
    if x==0 and y==0:
        print(i+1)
        break

if x!=0 or y!=0:
    print(-1)



