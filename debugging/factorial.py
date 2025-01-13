#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Vérification si un argument a été passé
if len(sys.argv) < 2:
    print("Erreur : Veuillez passer un argument pour le calcul du factoriel.")
else:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Erreur : L'argument doit être un nombre entier.")
