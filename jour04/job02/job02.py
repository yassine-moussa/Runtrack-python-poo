class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")
    
    def bonjour(self):
        print("Bonjour")
    
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=40):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

# Création d'un élève et d'un professeur
eleve1 = Eleve()
professeur1 = Professeur("maths", 40)

# Faire dire bonjour à l'élève et aller en cours
eleve1.bonjour() # Output : "Hello"
eleve1.allerEnCours() # Output : "Je vais en cours"

# Redéfinition de l'âge de l'élève à 15 ans
eleve1.modifierAge(15)

print("                                         ")
print("                                         ")

# Faire dire bonjour au professeur et commencer le cours
professeur1.bonjour() # Output : "Hello"
professeur1.enseigner() # Output : "Le cours va commencer"