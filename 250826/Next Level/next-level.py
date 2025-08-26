user2_id, user2_level = input().split()
user2_level = int(user2_level)

class User:
    def __init__(self, name, lv):
        self.n = f'user {name}'
        self.l = f'lv {lv}'

c = User('codetree', 10)
h = User(user2_id, user2_level)

print(c.n, c.l)
print(h.n, h.l)
