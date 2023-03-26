class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self._disponible = disponible

    def verification(self):
        return self._disponible

    def emprunter(self):
        if self.verification():
            self._disponible = False
            print("Le livre {} a été emprunté.".format(self.titre))
        else:
            print("Désolé, le livre {} n'est pas disponible pour le moment.".format(self.titre))

    def rendre(self):
        if not self.verification():
            self._disponible = True
            print("Le livre {} a été rendu.".format(self.titre))
        else:
            print("Le livre {} n'a pas été emprunté.".format(self.titre))

livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
livre2 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", False)

livre1.emprunter()  # Le livre Le Seigneur des Anneaux a été emprunté.
livre1.rendre()     # Le livre Le Seigneur des Anneaux a été rendu.

livre2.emprunter()  # Désolé, le livre Harry Potter à l'école des sorciers n'est pas disponible pour le moment.
livre2.rendre()     # Le livre Harry Potter à l'école des sorciers n'a pas été emprunté.