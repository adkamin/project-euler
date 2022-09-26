"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divisible_by_all(nr, divisors):
    for d in divisors:
        if nr % d != 0:
            return False
    return True

def find_nr(minimum, dividors):
    divisors = list(range(dividors,2,-1))
    i = minimum
    found = False
    while not found:
        if divisible_by_all(i, divisors):     
            found = True
        else:
            i += 10
    return i

print(find_nr(2520, 20))
