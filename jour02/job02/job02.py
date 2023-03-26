class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print("Titre du livre :", livre.get_titre()) # affiche "Le Petit Prince"
print("Auteur du livre :", livre.get_auteur()) # affiche "Antoine de Saint-Exupéry"
print("Nombre de pages du livre :", livre.get_nombre_de_pages()) # affiche 96

livre.set_titre("Les Misérables")
livre.set_auteur("Victor Hugo")
livre.set_nombre_de_pages(1500)
print("Nouveau titre du livre :", livre.get_titre()) # affiche "Les Misérables"
print("Nouvel auteur du livre :", livre.get_auteur()) # affiche "Victor Hugo"
print("Nouveau nombre de pages du livre :", livre.get_nombre_de_pages()) # affiche 1500

livre.set_nombre_de_pages(-100) # affiche "Le nombre de pages doit être un entier positif."
livre.set_nombre_de_pages("200") # affiche "Le nombre de pages doit être un entier positif."
