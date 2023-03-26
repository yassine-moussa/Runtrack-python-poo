class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=4, hauteur=3)

# Affichage en console du résultat de la méthode aire de la classe Rectangle
print("Aire du rectangle :", rectangle.aire())
