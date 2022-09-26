"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def find_max_factor(n):
    num = max_factor = n
    i = 2
    while i < num and max_factor >= num:
        if num % i == 0:
            max_factor = int(num / i)
            i = 2
            num = max_factor
        i += 1
    return max_factor

print(find_max_factor(600851475143))