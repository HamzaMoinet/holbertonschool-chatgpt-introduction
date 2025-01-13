#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: ./factorial_recursive.py <non-negative integer>")
            sys.exit(1)

        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Only non-negative integers are allowed.")

        f = factorial(n)
        print(f)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
