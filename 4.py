"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def biggest_palindrome(n):
    for i in range(n, 1, -1):
        if palindrome(0, len(str(i))-1, str(i)):
            for j in range(999, 1, -1):
                divider = i / j
                if divider <= 999 and (divider - int(divider) == 0):
                    print(f'Palindrome is {j} * {int(i / j)} = {i}')
                    return (i)

def palindrome(i, j, word):
    if i == j:
        return True
    if i == j-1:
        return word[i] == word[j]
    if word[i] == word[j]:
        return palindrome(i+1, j-1, word)
    else:
        False

print(biggest_palindrome(999*999))