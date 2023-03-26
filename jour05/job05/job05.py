def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nombre = int(input("Entrez un nombre entier : "))
print("Le", nombre, "ème nombre de la suite de Fibonacci est", fibonacci(nombre))
