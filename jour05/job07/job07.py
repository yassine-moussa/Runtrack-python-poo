def comparer_chaines(chaine1, chaine2):
    if chaine1 == chaine2:
        return 1
    elif '*' not in chaine2:
        return 0
    else:
        pos = chaine2.index('*')
        avant = chaine2[:pos]
        apres = chaine2[pos+1:]
        for i in range(len(chaine1) - len(avant) - len(apres) + 1):
            if chaine1[i:i+len(avant)] == avant and chaine1[i+len(avant):i+len(avant)+len(apres)] == apres:
                return 1
        return 0

ch1 = input("Entrez une première chaîne de caractères : ")
ch2 = input("Entrez une deuxième chaîne de caractères contenant des '*' : ")
if comparer_chaines(ch1, ch2):
    print("Les deux chaînes sont identiques.")
else:
    print("Les deux chaînes ne sont pas identiques.")
