class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}, Année : {self.annee}, Prix : {self.prix}")

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print("Je démarre ma voiture.")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roues}")

    def demarrer(self):
        print("Je démarre ma moto.")

# Instanciation de la classe Voiture et appel de la méthode "informationsVehicule"
voiture = Voiture(marque="Toyota", annee=2020, prix=25000)
voiture.informationsVehicule()

# Instanciation de la classe Moto et appel de la méthode "informationsVehicule"
moto = Moto(marque="Harley-Davidson", annee=2021, prix=15000)
moto.informationsVehicule()

# Appel de la méthode "demarrer" pour la voiture et la moto
voiture.demarrer()
moto.demarrer()
