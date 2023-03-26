class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Age de la personne:", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation des classes
personne = Personne()
eleve = Eleve()

# Affichage de l'âge de l'élève par défaut
eleve.affichageAge()
