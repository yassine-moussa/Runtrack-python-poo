def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])

ch = input("Entrez une chaine de caractères : ")
print("La longueur de la chaine", ch, "est", longueur(ch))
