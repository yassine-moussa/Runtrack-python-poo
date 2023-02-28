class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print("Nom :", self.nom)
        print("Prix HT :", self.prixHT, "€")
        print("TVA :", self.TVA, "%")
        print("Prix TTC :", self.CalculerPrixTTC(), "€")

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA

# création de produits
p1 = Produit("Livre", 10, 5.5)
p2 = Produit("Chaussures", 50, 20)
p3 = Produit("Macbook", 2000, 40)

# affichage des produits
p1.afficher()
p2.afficher()
p3.afficher()


# affichage du nouveau prix TTC du premier produit
print(p1.CalculerPrixTTC())