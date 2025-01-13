#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémente n pour éviter une boucle infinie
    return result

if __name__ == "__main__":
    try:
        # Vérifie que l'argument est un entier positif
        if len(sys.argv) != 2:
            print("Usage: python3 script.py <non-negative integer>")
            sys.exit(1)

        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Only non-negative integers are allowed")

        f = factorial(n)
        print(f)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
