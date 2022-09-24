"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = [2]

def is_prime(n):
    # print(n)
    for p in primes:
        # print(p)
        if n % p == 0:
            return False
    return True

def find_prime_number(n):
    prime = 3
    while len(primes) < n:
        # print(f'{len(primes)}')
        # print(f'testing number {prime}')
        if is_prime(prime):
            # print("prime!")
            primes.append(prime)
        prime += 2
    return primes[-1]

print(find_prime_number(10001))
