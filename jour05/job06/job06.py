def placer_dames(n):
    def est_valide(tab, i, j):
        for k in range(i):
            if tab[k] == j or abs(i - k) == abs(j - tab[k]):
                return False
        return True

    def backtrack(tab, i):
        if i == n:
            return True
        for j in range(n):
            if est_valide(tab, i, j):
                tab[i] = j
                if backtrack(tab, i+1):
                    return True
        return False

    tab = [-1] * n
    if not backtrack(tab, 0):
        print("Impossible de placer les dames.")
        return
    for i in range(n):
        for j in range(n):
            if tab[i] == j:
                print(" X ", end="")
            else:
                print(" O ", end="")
        print()

n = int(input("Entrez un nombre entier : "))
placer_dames(n)
