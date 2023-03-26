class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def __str__(self):
        return f"Rectangle(longueur={self.__longueur}, largeur={self.__largeur})"


rect = Rectangle(10, 5)
print(rect)

rect.set_longueur(12)
rect.set_largeur(6)
print(rect)

print(f"Longueur : {rect.get_longueur()}") 
