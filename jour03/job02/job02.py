class CompteBancaire:
    
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        
    def afficher(self):
        print("Numéro de compte : ", self.__numero_compte)
        print("Nom et prénom : ", self.__nom, self.__prenom)
        print("Solde : ", self.__solde)
        print("Découvert autorisé : ", self.__decouvert)
        
    def afficherSolde(self):
        print("Le solde du compte est de ", self.__solde, " euros.")
        
    def versement(self, montant):
        self.__solde += montant
        print("Le montant de ", montant, " euros a bien été versé.")
        self.afficherSolde()
        
    def retrait(self, montant):
        if self.__decouvert or self.__solde >= montant:
            self.__solde -= montant
            print("Le montant de ", montant, " euros a bien été retiré.")
            self.afficherSolde()
        else:
            print("Opération impossible : solde insuffisant et découvert non autorisé.")
        
    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05 # frais de 5% pour un découvert
            self.__solde -= frais
            print("Des agios de ", frais, " euros ont été appliqués.")
            self.afficherSolde()
            
    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            print("Le virement de ", montant, " euros a bien été effectué vers le compte ", compte_destinataire.__numero_compte)
            self.afficherSolde()
        else:
            print("Opération impossible : solde insuffisant.")

# Création d'un compte avec un solde de 1000 euros
compte1 = CompteBancaire("4987 4523 0147 7453", "Dupont", "Jean", 1000)

# Affichage des informations sur le compte
compte1.afficher()

# Versement de 500 euros
compte1.versement(500)

# Retrait de 200 euros
compte1.retrait(200)

# Tentative de retrait de 1500 euros (solde insuffisant)
compte1.retrait(1500)

# Ajout de l'attribut découvert
compte2 = CompteBancaire("2697 4523 1472 0320", "Martin", "Sophie", -500, True)

# Application des agios
compte2.agios()

# Virement du compte 1 vers le compte 2
compte1.virement(compte2, 700)