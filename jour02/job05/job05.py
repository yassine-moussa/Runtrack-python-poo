class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("La voiture n'a pas assez d'essence pour démarrer.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else:
            return False


# création d'une instance de la classe "Voiture"
ma_voiture = Voiture("Renault", "Clio", 2015, 10000)

# affichage de la marque de la voiture
print(ma_voiture.get_marque())  # Renault

# mise à jour de la marque de la voiture
ma_voiture.set_marque("Peugeot")

# affichage de la marque mise à jour
print(ma_voiture.get_marque())  # Peugeot

# mise en marche de la voiture
ma_voiture.demarrer()

# affichage de l'état de marche de la voiture
print(ma_voiture.get_en_marche())  # True

# arrêt de la voiture
ma_voiture.arreter()

# affichage de l'état de marche de la voiture
print(ma_voiture.get_en_marche())  # False