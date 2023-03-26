def puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        p = puissance(x, n/2)
        return p * p
    else:
        return x * puissance(x, n-1)

x = int(input("Entrez un nombre entier x : "))
n = int(input("Entrez un nombre entier n : "))
print("x^n =", puissance(x, n))
