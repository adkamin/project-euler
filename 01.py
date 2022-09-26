"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_sum(prime1, prime2):
    sum = 0
    for i in range(prime1, 1000, prime1):
        sum += i
    for i in range(prime2, 1000, prime2):
        if i % prime1 != 0:
            sum += i
    return sum

print(find_sum(3, 5))