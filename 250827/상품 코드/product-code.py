product_name, product_code = input().split()
product_code = int(product_code)

class pr:
    def __init__(self, name, code):
        self.name = name
        self.code = code

p1 = pr('codetree', 50)
p2 = pr(product_name, product_code)

print(f'product {p1.code} is {p1.name}')
print(f'product {p2.code} is {p2.name}')