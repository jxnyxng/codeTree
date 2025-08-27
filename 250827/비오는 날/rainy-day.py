n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class Rain:
    def __init__(self, date, day, weather): 
        self.date = date
        self.day = day
        self.weather = weather 


gu=[]
for i in range(n):
    if weather[i]=='Rain':
        r = Rain(date[i], day[i], weather[i])
        gu.append(r)

gu.sort(key=lambda g:g.date)
print(gu[0].date, gu[0].day, gu[0].weather)