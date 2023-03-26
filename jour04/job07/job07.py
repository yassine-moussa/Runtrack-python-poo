import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return str(self.valeur) + " de " + self.couleur

class Jeu:
    def __init__(self):
        valeurs = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"]
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        self.paquet = []
        for valeur in valeurs:
            for couleur in couleurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger(self):
        random.shuffle(self.paquet)

    def donner_carte(self):
        carte = self.paquet.pop()
        return carte

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def vider_main(self):
        self.main = []

    def calculer_points(self):
        total = 0
        as_present = False
        for carte in self.main:
            if isinstance(carte.valeur, int):
                total += carte.valeur
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            else:
                as_present = True
                total += 1
        if as_present and total <= 11:
            total += 10
        return total

    def afficher_main(self):
        print(self.nom + " a en main :")
        for carte in self.main:
            print(carte)

# Exemple d'utilisation
joueur = Joueur("Bob")
jeu = Jeu()
jeu.melanger()
joueur.ajouter_carte(jeu.donner_carte())
joueur.ajouter_carte(jeu.donner_carte())
joueur.afficher_main()
points = joueur.calculer_points()
print("Total de points : " + str(points))
