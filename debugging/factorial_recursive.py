#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a given integer.

    Parameters:
    n (int): An integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the integer `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read input from the command line and compute the factorial
f = factorial(int(sys.argv[1]))
print(f)
