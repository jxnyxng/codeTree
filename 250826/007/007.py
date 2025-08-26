secret_code, meeting_point, time = input().split()
time = int(time)

class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.s = f'secret code : {secret_code}'
        self.m = f'meeting point : {meeting_point}'
        self.t = f'time : {time}'

secret1 = Secret(secret_code, meeting_point, time)
print(secret1.s)
print(secret1.m)
print(secret1.t)