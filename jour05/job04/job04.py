def plus_grand_chiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        max_chiffre = plus_grand_chiffre(liste[1:])
        if liste[0] > max_chiffre:
            return liste[0]
        else:
            return max_chiffre


