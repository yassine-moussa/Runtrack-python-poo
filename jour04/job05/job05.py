import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius * self.radius

# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=4, hauteur=3)

# Instanciation de la classe Cercle
cercle = Cercle(radius=5)

# Affichage en console du résultat de la méthode aire pour chaque instance
print("Aire du rectangle :", rectangle.aire())
print("Aire du cercle :", cercle.aire())
