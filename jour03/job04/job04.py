class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Nom: {self.nom}\nNuméro: {self.numero}\nPosition: {self.position}\nButs: {self.buts}\nPasses décisives: {self.passes_decisives}\nCartons jaunes: {self.cartons_jaunes}\nCartons rouges: {self.cartons_rouges}\n")


class Equipe:
    def __init__(self, nom, liste_joueurs=None):
        self.nom = nom
        self.liste_joueurs = liste_joueurs or []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        joueur.buts += buts
        joueur.passes_decisives += passes_decisives
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges

# Création des joueurs
joueur1 = Joueur("Lionel Messi", 10, "attaquant")
joueur2 = Joueur("Cristiano Ronaldo", 7, "attaquant")
joueur3 = Joueur("Neymar Jr", 11, "attaquant")
joueur4 = Joueur("Luka Modric", 19, "milieu")
joueur5 = Joueur("Sergio Ramos", 4, "défenseur")

# Création des équipes
equipe1 = Equipe("Equipe 1")
equipe2 = Equipe("Equipe 2")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)

equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur5)

# Présentation des joueurs de chaque équipe
print("Équipe 1:")
equipe1.afficherStatistiquesJoueurs()

print("\nÉquipe 2:")
equipe2.afficherStatistiquesJoueurs()

# Simulation de match (marquer un but, avoir un carton rouge, etc.)
joueur1.marquerUnBut()
joueur3.marquerUnBut()
joueur4.effectuerUnePasseDecisive()
joueur5.recevoirUnCartonJaune()
joueur2.recevoirUnCartonRouge()

# Mise à jour des statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur(joueur1, buts=1)
equipe2.mettreAJourStatistiquesJoueur(joueur3, buts=1, passes_decisives=1)
equipe2.mettreAJourStatistiquesJoueur(joueur4, passes_decisives=1)
equipe2.mettreAJourStatistiquesJoueur(joueur5, cartons_jaunes=1)
equipe1.mettreAJourStatistiquesJoueur(joueur2, cartons_rouges=1)

# Affichage à nouveau des statistiques des joueurs
print("Statistiques des joueurs après simulation de match:")
print("\nÉquipe 1:")
equipe1.afficherStatistiquesJoueurs()

print("\nÉquipe 2:")
equipe2.afficherStatistiquesJoueurs()




