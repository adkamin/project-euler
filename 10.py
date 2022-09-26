"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time

primes = [2]

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True

def find_prime_number(n):
    start_time = time.time()
    prime = 3
    sum_primes = 2
    while prime < n:
        if is_prime(prime):
            primes.append(prime)
            sum_primes += prime
        prime += 2
    print("the program took %s seconds" % (time.time() - start_time))
    return sum_primes

print(find_prime_number(2000000))