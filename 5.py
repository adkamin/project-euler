"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divisible_by_all(nr, divisors):
    for d in divisors:
        if nr % d != 0:
            return False
    return True

def find_nr():
    divisors = list(range(20,2,-1))
    i = 2520
    found = False

    while not found:
        if divisible_by_all(i, divisors):     
            found = True
        else:
            i += 10
    return i

print(find_nr())
