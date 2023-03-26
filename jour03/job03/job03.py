class Tache:
    def __init__(self, titre, description, statut='à faire'):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Titre: {self.titre}\nDescription: {self.description}\nStatut: {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminer"

    def afficherListe(self):
        for tache in self.taches:
            print(tache, "\n")

    def filtrerListe(self, statut):
        liste_filtree = [tache for tache in self.taches if tache.statut == statut]
        return liste_filtree


# Test du code
liste = ListeDeTaches()

tache1 = Tache("Acheter du lait", "Acheter 2 litres de lait à l'épicerie")
tache2 = Tache("Payer les factures", "Payer les factures d'électricité et d'eau")
tache3 = Tache("Répondre aux e-mails", "Répondre aux e-mails importants du travail")

# Ajouter les tâches à la liste
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# Afficher la liste des tâches
print("Liste des tâches:")
liste.afficherListe()

# Supprimer une tâche
liste.supprimerTache(tache2)
print("Liste des tâches après suppression:")
liste.afficherListe()

# Marquer une tâche comme terminée
liste.marquerCommeFinie(tache1)
print("Liste des tâches après marquage comme terminée:")
liste.afficherListe()

# Afficher toutes les tâches
print("Toutes les tâches:")
liste.afficherListe()

# Afficher les tâches à faire
print("Tâches à faire:")
taches_a_faire = liste.filtrerListe("à faire")
for tache in taches_a_faire:
    print(tache, "\n")

# Afficher les tâches terminées
print("Tâches terminées:")
taches_terminees = liste.filtrerListe("terminer")
for tache in taches_terminees:
    print(tache, "\n")


