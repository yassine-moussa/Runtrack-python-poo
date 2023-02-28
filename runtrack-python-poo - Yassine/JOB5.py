
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Le point a pour coordonnées ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")

    def afficherXchangé(self):
        print(f"La coordonnée changée de x est : {self.x}")

    def afficherYchangé(self):
        print(f"La coordonnée changée de y est : {self.y}")

    def changerX(self, new_x):
        self.x = new_x

    def changerY(self, new_y):
        self.y = new_y
point1 = Point(3, 5) #instance point

# Afficher les coordonnées du point
point1.afficherLesPoints() 
# Afficher les valeurs repective de x et y
point1.afficherX() 
point1.afficherY() 
# Modification de la valeur  x
point1.changerX(9)
point1.afficherXchangé() 
# Modification de la valeur  y
point1.changerY(3)
point1.afficherYchangé() 