class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants

    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.set_nb_habitants(self.__ville.get_nb_habitants() + 1)


# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants des villes
print(f"Nombre d'habitants de {paris.get_nom()}: {paris.get_nb_habitants()}")
print(f"Nombre d'habitants de {marseille.get_nom()}: {marseille.get_nb_habitants()}")
