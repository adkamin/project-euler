"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def find_difference(n):
    sum = sum_of_squares = 0
    for i in range(1,n+1):
        sum_of_squares += i**2
        sum += i
    diff = sum**2 - sum_of_squares
    return(diff)

print(find_difference(100))
