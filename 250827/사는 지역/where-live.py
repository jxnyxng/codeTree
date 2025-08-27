n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class A:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

person = []
for i in range(n):
    a = A(name[i], street_address[i], region[i])
    person.append(a)

person.sort(key=lambda person:person.name)

print('name', person[-1].name)
print('addr', person[-1].street_address)
print('city', person[-1].region)


