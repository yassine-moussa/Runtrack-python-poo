import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau de difficulté (1 - facile, 2 - moyen, 3 - difficile) : "))

    def lancerJeu(self):
        if self.niveau == 1:
            Sub_Zero = 100
            Scorpion = 50
        elif self.niveau == 2:
            Sub_Zero = 75
            Scorpion = 75
        elif self.niveau == 3:
            Sub_Zero = 50
            Scorpion = 100
        else:
            print("Niveau invalide.")
            return

        joueur = Personnage("Joueur", Sub_Zero)
        ennemi = Personnage("Ennemi", Scorpion)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print("Le joueur a vaincu l'ennemi.")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print("L'ennemi a vaincu le joueur.")
                break

            print(f"Vie restante du joueur: {joueur.vie}, vie restante de l'ennemi: {ennemi.vie}\n")

# Lancement du jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

if __name__ == "__main__":
    main()

