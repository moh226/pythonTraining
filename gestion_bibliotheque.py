class Auteur :

    def __init__(self, nom, prenom, nationalite) :
        self.nom = nom
        self.prenom = prenom
        self.nationalite = nationalite

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.nationalite})"



class Livre:
    def __init__(self, titre, auteur, annee, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible

    def __str__(self):
        return f"{self.titre} - {self.auteur.nom} {self.auteur.prenom} ({self.annee}) | {'disponible' if self.disponible else 'non disponible'}"



class Bibliotheque:
    def __init__(self, nom) :
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre) :
        self.livres.append(livre)

    def affiche_livres(self) :
        for livre in self.livres:
            print(livre)

    def recherche_livres(self, titre) :
        for livre in self.livres:
            if livre.titre == titre:
                print(livre)
                return
        print("Livre non disponible")

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                if livre.disponible:
                    print("livre emprunter")
                    livre.disponible = False
                    return
                else:
                    print("Livre deja emprunter")
                    return
        print("Livre non disponible")


    def retourner_livre(self, titre) :
        for livre in self.livres:
            if livre.titre == titre:
                if livre.disponible:
                    print("ce livre n'a pas été emprunter")
                    return
                else:
                    livre.disponible = True
                    print("Livre retourné avec succès !")
                    return
        print("Livre non disponible")



a = Auteur("Hugo", "Victor", "Français")
l = Livre("Les miserables", a, 1862)

b = Bibliotheque("Médiathèque centrale")
b.ajouter_livre(l)

b.affiche_livres()
b.emprunter_livre("Les miserables")
b.emprunter_livre("Les miserables")
b.retourner_livre("Les miserables")
b.retourner_livre("Les miserables")
b.retourner_livre("Germinal")