"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from math import sqrt

def find_product(n):
    for i in range(n):
        for j in range(n):
            c_squared = i**2 + (i+j)**2
            if i + (i+j) + sqrt(c_squared) == n:
                if i < (i+j) and (i+j) < sqrt(c_squared):
                    product = i * (i+j) * int(sqrt(c_squared))
                    print(f'{i} * {i+j} * {int(sqrt(c_squared))} = {product}')
                    return product

print(find_product(1000))