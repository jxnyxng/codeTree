n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)] 
# x y 각각 증가시켜보면서 나뉘는 결과가 1 2 3 4분면에 균등히 위치하는 지점 찾기

# for문으로 x,y 지정
# 주어진 좌표가 그은 선분과 비교 1 2 3 4분면에 위치한 개수 세기
# 가장 많은 개수 세고
# 그 개수의 최솟값만 저장

# print(ymin, ymax, xmin, xmax)
ans=float('inf')
for i in range(2, 102, 2): # x
    for j in range(2, 102, 2): # y 
        a,b,c,d = 0,0,0,0

        for k in range(n):
            # 1
            if i < points[k][0] and points[k][1] > j:
                a+=1
            # 2
            if i > points[k][0] and points[k][1] > j:
                b+=1
            # 3
            if i > points[k][0] and points[k][1] < j:
                c+=1
            # 4
            if i < points[k][0] and points[k][1] < j:
                d+=1 
       
        te = max([a,b,c,d])
        # print(te)
        ans=min(ans,te)

print(ans)