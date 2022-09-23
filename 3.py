"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

num = max_factor = 600851475143
i = 2
while i < num and max_factor >= num:
    if num % i == 0:
        max_factor = int(num / i)
        i = 2
        num = max_factor
    i+=1

print(max_factor)