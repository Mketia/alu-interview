#!/usr/bin/python3

"""
A function that computes the minimum number of operations
needed to produce exactly n 'H' characters in the file.
"""

def minOperations(n):
    """
    Determines the fewest operations required to generate exactly 
    n 'H' characters in the file.
    
    :param n: The desired number of 'H' characters
    :type n: int
    :return: The minimum number of required operations
    """
    if n <= 1:
        return 0

    i = 2
    results = 0

    while i <= n:
        if n % i == 0:
            results += i
            n = n / i  # or n //= i
        else:
            i += 1
 return results
